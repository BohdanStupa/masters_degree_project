import numpy as np


class ChambollePockAlgorithm:

    def __init__(
        self,
        *,
        n_iter: int,
        tau: float,
        sigma: float,
        theta: float,
        h: float,
        logger,
        image_progress_update_frequency: int = 0,
        eps: float = 1e-6,
    ):
        self._n_iter = n_iter
        self._tau = tau
        self._sigma = sigma
        self._theta = theta
        self._eps = eps
        self._h = h
        self._logger = logger

    def run_chambolle_pock_algorithm(self, x, y,  K, K_star, f, res_F, res_G, j_tv) -> np.ndarray:
        x_bar = x.copy()
        x_old = x.copy()

        self._logger.info('====================================================================')
        self._logger.info('Iter:\tdX:\t\tJ(u):\t\tf:\t\tPrimal objective:')
        for n in range(self._n_iter):
            err = np.linalg.norm(x-x_old)
            ju = j_tv(x)
            fu = np.sum(f*x)
            obj = fu + ju
            # print("{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(n, err, ju, fu, obj))
            self._logger.info("{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(n, err, ju, fu, obj))
            if (err < self._eps) and (n > 0):
                break
            x_old = x.copy()
            y = res_F(y + self._sigma * K(x_bar))
            x = res_G(x - self._tau * (K_star(y)+f))
            x_bar = x + self._theta * (x - x_old)
        return x
