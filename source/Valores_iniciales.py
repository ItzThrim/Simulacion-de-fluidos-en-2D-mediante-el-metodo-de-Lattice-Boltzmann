import numpy as np

# Constantes globales
M = np.array([
    [0, 0], [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, 1], [-1, -1], [1, -1]
])
pesos = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])
w = 2  # Parámetro de relajación

def inicializar_red(Nx, Ny, vx_inicial=0.1):
    mat_vel = np.zeros((Nx, Ny, 2))
    mat_den = np.ones((Nx, Ny))
    f = np.zeros((Nx, Ny, 9))
    mat_vel[:, :, 0] = vx_inicial
    return mat_vel, mat_den, f
