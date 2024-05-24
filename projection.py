import numpy as np


def project_balls(p):
    """ Projection onto unit balls."""
    pt = np.transpose(p, (0,1,3,2))
    n = np.linalg.norm(pt, axis = 3)
    d = np.maximum(2*n, 1)
    for i in range(pt.shape[3]):
        pt[:,:,:,i] = pt[:,:,:,i]/d
    p = np.transpose(pt, (0,1,3,2))
    return p


def project_simplex(u):
    (ny, nx, k) = u.shape

    def proj_prob(xv):
        x = np.array(xv)
        if not len(x.shape) == 1:
            return 1.
        D = x.shape[0]
        uv = np.sort(x)[::-1]
        vv = uv + np.array([1./j - np.sum(uv[0:j])/float(j) for j in range(1,D+1)])
        rho = np.max(np.where(vv > 0))
        lmbda = (1 - np.sum(uv[0:rho+1]))/float(rho+1)
        xp = np.maximum(x + lmbda, 0)
        return xp

    for i in range(ny):
        for j in range(nx):
            u[i,j,:] = proj_prob(np.squeeze(u[i,j,:]))
    return u
