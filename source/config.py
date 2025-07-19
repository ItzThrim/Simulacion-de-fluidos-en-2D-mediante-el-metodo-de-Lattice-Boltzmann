import numpy as np

Nx = 120
Ny = 60
u0 = 0.1
viscosidad = 0.8
tau = 3 * viscosidad + 0.5
w = 1 / tau

M = np.array([
    [0, 0],
    [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, 1], [-1, -1], [1, -1]
])
pesos = np.array([4/9] + [1/9]*4 + [1/36]*4)
opuestos = [0, 3, 4, 1, 2, 7, 8, 5, 6]