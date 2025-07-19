import numpy as np
from config import Nx, Ny, u0, M, pesos
#mer y segundo paso del algoritmo en Python, que es realizar la red (Matriz) y dar inicio a la densidad y las velocidades
#ctrl + s

def crear_triangulo():
    Obs = np.zeros((Nx, Ny), dtype=bool)
    x1, y1 = 20, 30
    x2, y2 = 60, 15
    x3, y3 = 60, 45
    denom = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))

    for i in range(Nx):
        for j in range(Ny):
            if denom == 0:
                continue
            a = ((y2 - y3)*(i - x3) + (x3 - x2)*(j - y3)) / denom
            b = ((y3 - y1)*(i - x3) + (x1 - x3)*(j - y3)) / denom
            c = 1 - a - b
            if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
                Obs[i, j] = True
    return Obs


def inicializar(Obs=None):
    """Inicializa densidad, velocidad y distribución."""
    if Obs is None:
        Obs = np.zeros((Nx, Ny), dtype=bool)
    
    f = np.zeros((Nx, Ny, 9))
    rho = np.ones((Nx, Ny))
    vx = np.where(np.arange(Nx)[:, None] < 5, u0, 0)  # Perfil de velocidad inicial
    vy = np.zeros((Nx, Ny))
    
    # Distribución inicial en equilibrio
    for k in range(9):
        v = M[k]
        pp = v[0] * vx + v[1] * vy
        v2 = vx**2 + vy**2
        f[:, :, k] = pesos[k] * rho * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
    
    return f, rho, vx, vy, Obs


def condiciones_frontera(f, vx, vy, rho):
    for j in range(Ny):
        vx[0, j] = u0
        vy[0, j] = 0
        rho[0, j] = np.sum(f[0, j])
        for k in range(9):
            v = M[k]
            pp = v[0]*vx[0, j] + v[1]*vy[0, j]
            v2 = vx[0, j]**2 + vy[0, j]**2
            f[0, j, k] = pesos[k] * rho[0, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
        for k in range(9):
            f[-1, j, k] = f[-2, j, k]
    return f
