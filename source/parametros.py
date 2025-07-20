import numpy as np
import os

Nx = 60
Ny = 30
u0 = 0.1
viscosidad = 0.5
tau = 3 * viscosidad + 0.5
w = 1 / tau
paso_de_tiempo = 250
guardar_cada = 5

M = np.array([
    [0, 0],
    [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, 1], [-1, -1], [1, -1]
])
pesos = np.array([4/9] + [1/9]*4 + [1/36]*4)
#Direcciones para el rebote
opuestos = [0, 3, 4, 1, 2, 7, 8, 5, 6]
