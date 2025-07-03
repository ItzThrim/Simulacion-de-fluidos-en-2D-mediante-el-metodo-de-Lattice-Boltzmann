import numpy as np

def inicializar_red(Nx, Ny, vx_inicial=0.1):

    mat_vel = np.zeros((Nx, Ny, 2))
    mat_den = np.ones((Nx, Ny))
    f = np.zeros((Nx, Ny, 9))

    mat_vel[:, :, 0] = vx_inicial

    return mat_vel, mat_den, f
