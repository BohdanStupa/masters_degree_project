import numpy as np
import cv2
from sklearn.cluster import KMeans

from pathlib import Path

from chambole_pock_algorithm import ChambollePockAlgorithm
from projection import project_balls, project_simplex
from logger import get_custom_logger


def grad(u, h) -> np.ndarray:
    p = np.zeros((u.shape[0], u.shape[1], 2, u.shape[2]))
    for i in range(u.shape[2]):
        p[0:-1, :, 0, i] = (u[1:, :, i] - u[0:-1, :, i])/h
        p[:, 0:-1, 1, i] = (u[:, 1:, i] - u[:, 0:-1, i])/h
    return p


def div(p, h) -> np.ndarray:
    u = np.zeros((p.shape[0], p.shape[1], p.shape[3]))
    for i in range(p.shape[3]):
        u[1:,:,i]  = (p[1:, :, 0, i] - p[0:-1, :, 0, i])/h
        u[:,1:,i] += (p[:, 1:, 1, i] - p[:, 0:-1, 1, i])/h
    return u


def J1(x, h) -> np.ndarray:
    return np.sum(np.linalg.norm(grad(x,h), axis = 2))


def get_centers(img: np.ndarray, nc: int = 16) -> np.ndarray:
    ny = img.shape[0]
    nx = img.shape[1]
    N = nx * ny
    X = img.reshape(N, -1, 3).squeeze()

    km = KMeans(n_clusters = nc).fit(X)
    return km.cluster_centers_


def load_image(path_to_image: Path) -> np.ndarray:
    if not path_to_image.exists():
        raise FileNotFoundError(path_to_image)

    img = cv2.imread(str(path_to_image))
    im_height, im_width, *_ = img.shape
    new_width = 760
    new_height = int((new_width / im_width) * im_height)
    img = cv2.resize(img, (new_width, new_height))
    return img


def mumford_shah(path_to_image: Path, n_iter: int, lmbda: float, theta: float, tau: float, h: float, n_clasters: int):
    log_path = f'logs/{path_to_image.stem}_MS_lambda={lmbda}.theta={theta}.tau={tau}.h={h}.n_iter={n_iter}'
    logs_dir = Path("logs")
    logs_dir.mkdir(parents=True, exist_ok=True)
    _logger = get_custom_logger('', log_path)

    _logger.info('=============================================================================================')
    _logger.info(f'Chambolle-Pock algorithm for Mumford-Shah image segmentation. Number of iterations: {n_iter}')
    _logger.info(f'Regularization (smaller = smoother): lambda ={lmbda}')
    _logger.info(f'Configs: {theta=}, {tau=}, {h=}')

    L2 = 8 / h**2
    sigma = 1 / (L2 * tau)

    res_F = project_balls
    res_G = project_simplex
    K = lambda x: grad(x, h)
    K_star = lambda x: -div(x, h)
    j_tv = lambda x: J1(x, h)

    image = load_image(path_to_image)
    ny, nx, *_ = image.shape

    # Start with a better initial guess based on k-means clustering
    # Generate set of images, f_l, that are the error measures for each pixel and each color, c_l, obtained from k-means

    n_of_guessing_segments = n_clasters
    _logger.info(f'Start with a better initial guess based on k-means clustering: {n_of_guessing_segments}')
    centers = get_centers(image, n_of_guessing_segments)
    f = np.zeros((ny, nx, n_of_guessing_segments))
    for c in range(n_of_guessing_segments):
        for i in range(ny):
            for j in range(nx):
                f[i, j, c] = lmbda*(np.linalg.norm(image[i, j, :]-centers[c, :]))**2 / 2

    u = res_G(np.zeros((ny, nx, n_of_guessing_segments)))
    p = res_F(K(u))

    solver = ChambollePockAlgorithm(
        n_iter=n_iter,
        theta=theta,
        tau=tau,
        sigma=sigma,
        h=h,
        logger=_logger,
    )
    u_s = solver.run_chambolle_pock_algorithm(u, p, K, K_star, f, res_F, res_G, j_tv)

    # Take argmax of u tensor to obtain segmented image
    # Paint the image by the cluster colors
    ms_img = np.zeros(image.shape)
    for i in range(ny):
        for j in range(nx):
            col = np.argmax(u_s[i,j,:])
            ms_img[i,j,:] += centers[col,:]

    ms_img = ms_img.astype(np.uint8)

    output_path = f'result/{path_to_image.stem}_MS_lambda={lmbda}.theta={theta}.tau={tau}.h={h}.n_iter={n_iter}.png'
    output_dir = Path("result")
    output_dir.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(output_path, ms_img)
    return ms_img
