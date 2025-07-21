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

def crear_obstaculo_circulo(xc, yc, radio):
    Obs = np.zeros((Nx, Ny), dtype=bool)
    for i in range(Nx):
        for j in range(Ny):
            if (i - xc)**2 + (j - yc)**2 <= radio**2:
                Obs[i, j] = True
    return Obs

def crear_obstaculo_rectangulo(x1, y1, x2, y2):
    Obs = np.zeros((Nx, Ny), dtype=bool)
    for i in range(Nx):
        for j in range(Ny):
            if x1 <= i <= x2 and y1 <= j <= y2:
                Obs[i, j] = True
    return Obs

def crear_obstaculo_vaca(x, y):
    Obs = np.zeros((Nx, Ny), dtype=bool)

    # Centro de la figura
    xc, yc = x // 2, y // 2

    # 1. Cuerpo (elipse grande)
    a_body, b_body = 12, 7
    for i in range(x):
        for j in range(y):
            xo, yo = i - xc, j - yc
            if (xo**2 / a_body**2 + yo**2 / b_body**2) <= 1:
                Obs[i, j] = True

    # 2. Cabeza (elipse más pequeña)
    a_head, b_head = 7, 4
    head_center = (xc + a_body - 25, yc + 8)
    for i in range(x):
        for j in range(y):
            xo, yo = i - head_center[0], j - head_center[1]
            if (xo**2 / a_head**2 + yo**2 / b_head**2) <= 1:
                Obs[i, j] = True

    # 3. Patas (rectángulos)
    leg_width, leg_height = 4, 10
    for leg_x in [xc - 7, xc + 9]:
        for i in range(leg_x - leg_width // 2, leg_x + leg_width // 2):
            for j in range(yc - b_body, yc - b_body - leg_height, -1):
                if 0 <= i < x and 0 <= j < y:
                    Obs[i, j] = True

    return Obs
def crear_obstaculo_vacio(x, y):
    Obs = np.zeros((x, y), dtype=bool)
    return Obs