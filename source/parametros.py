import numpy as np
import os

# Aca definimos los parametros del modelo, mantenga discresion con los valores

Nx = 20
Ny = 10
u0 = 0.1
viscosidad = 0.5
tau = 3 * viscosidad + 0.5
w = 1 / tau
paso_de_tiempo = 30
guardar_cada = 5

# La matriz del metodo, se explica en la parte teorica

M = np.array([
    [0, 0],
    [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, 1], [-1, -1], [1, -1]
])

# La funcion de pesos asociada a la funcion de equilibrio, le dmaos mas importancia a la criz del centro

pesos = np.array([4/9] + [1/9]*4 + [1/36]*4)
#Direcciones para el rebote
opuestos = [0, 3, 4, 1, 2, 7, 8, 5, 6]
