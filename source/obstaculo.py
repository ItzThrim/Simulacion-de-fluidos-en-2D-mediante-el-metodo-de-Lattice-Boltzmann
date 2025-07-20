import numpy as np
from parametros import Nx, Ny

#Aca creamos el objeto, yo deje el triangulo 


def crear_obstaculo_triangulo(x1, y1, x2, y2, x3, y3):
    Obs = np.zeros((Nx, Ny), dtype=bool)
    for i in range(Nx):
        for j in range(Ny):
            denom = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
            a = ((y2-y3)*(i-x3) + (x3-x2)*(j -y3)) / denom
            b = ((y3-y1)*(i-x3) + (x1-x3)*(j -y3)) / denom
            c = 1 - a - b
            if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
                Obs[i, j] = True
    return Obs