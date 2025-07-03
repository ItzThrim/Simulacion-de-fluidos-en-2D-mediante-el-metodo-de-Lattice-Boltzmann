# simulacion_lb.py
import numpy as np
from Valores_iniciales import inicializar_red

M = np.array([
    [0, 0], [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, 1], [-1, -1], [1, -1]
])
pesos = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])
w = 1.0

def calcular_equilibrio(d, v):
    feq = np.zeros(9)
    vv = np.dot(v, v)
    for k in range(9):
        V = M[k]
        Vv = np.dot(V, v)
        feq[k] = d * pesos[k] * (1 + 3 * Vv - 1.5 * vv + 4.5 * Vv**2)
    return feq

def actualizar_equilibrio_global(f, mat_den, mat_vel):
    Nx, Ny = mat_den.shape
    for i in range(Nx):
        for j in range(Ny):
            f[i, j, :] = calcular_equilibrio(mat_den[i, j], mat_vel[i, j])
    return f

def colisionar(f, w):
    fcol = np.copy(f)
    Nx, Ny, _ = f.shape
    for i in range(Nx):
        for j in range(Ny):
            feq = calcular_equilibrio(np.sum(f[i, j]), np.dot(f[i, j], M))
            for k in range(9):
                fcol[i, j, k] -= w * (fcol[i, j, k] - feq[k])
    return fcol

def propagar(fcol):
    Nx, Ny, _ = fcol.shape
    fprop = np.zeros_like(fcol)
    for i in range(Nx):
        for j in range(Ny):
            for k in range(9):
                inew = (i + M[k, 0]) % Nx
                jnew = (j + M[k, 1]) % Ny
                fprop[inew, jnew, k] = fcol[i, j, k]
    return fprop

def recalcular_macros(fprop):
    Nx, Ny, _ = fprop.shape
    mat_den = np.zeros((Nx, Ny))
    mat_vel = np.zeros((Nx, Ny, 2))
    for i in range(Nx):
        for j in range(Ny):
            mat_den[i, j] = np.sum(fprop[i, j])
            mat_vel[i, j] = np.dot(fprop[i, j], M)
    return mat_den, mat_vel