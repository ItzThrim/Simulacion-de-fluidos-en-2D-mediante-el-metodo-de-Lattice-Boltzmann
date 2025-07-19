import numpy as np
from config import Nx, Ny, M, pesos, opuestos, w
from Valores_iniciales import crear_triangulo, inicializar, condiciones_frontera


def colision(f, rho, vx, vy, Obs):
    """Paso de colisión BGK."""
    # Calcular densidad y velocidades (vectorizado)
    rho = np.sum(f, axis=2)
    vx = np.sum(f * M[:, 0].reshape(1, 1, -1), axis=2) / rho
    vy = np.sum(f * M[:, 1].reshape(1, 1, -1), axis=2) / rho
    
    # Reset obstáculos
    vx[Obs] = 0
    vy[Obs] = 0
    rho[Obs] = 1
    
    # Calcular distribución de equilibrio
    f_eq = np.zeros_like(f)
    for k in range(9):
        v = M[k]
        pp = v[0] * vx + v[1] * vy
        v2 = vx**2 + vy**2
        f_eq[:, :, k] = pesos[k] * rho * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
    
    # Relajación
    f = (1 - w) * f + w * f_eq
    return f, rho, vx, vy
def propagacion(f):
    f_propagacion = np.copy(f)
    for k in range(9):
        dx, dy = M[k]
        for i in range(Nx):
            for j in range(Ny):
                ni, nj = i + dx, j + dy
                if 0 <= ni < Nx and 0 <= nj < Ny:
                    f[ni, nj, k] = f_propagacion[i, j, k]
    return f, f_propagacion

def rebote(f, Obs):
    f_new = np.copy(f)
    for i in range(Nx):
        for j in range(Ny):
            if Obs[i, j]:
                for k in range(9):
                    f_new[i, j, k] = f[i, j, opuestos[k]]
    return f_new