import numpy as np
from parametros import Nx, Ny, u0, viscosidad, tau, w, paso_de_tiempo, guardar_cada, M, pesos, opuestos



def flujo(x,y,ux,uy,Mat,fun,v0,wh,drho):
# Flujo constante en izquierda Condición inicial
  for i in range(x):
      for j in range(y):
          if i < 10:
            ux[i, j] = v0
              #vx[-i,j] = -u0
          for k in range(9):
              v = Mat[k]
              pp = v[0] * ux[i, j] + v[1] * uy[i, j]
              v2 = ux[i, j]**2 + uy[i, j]**2
              fun[i, j, k] = wh[k] * drho[i, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
  return fun, ux, uy

def colision(x,y,drho,ux,uy,obj,fun):

    for i in range(x):
        for j in range(y):
            drho[i, j] = np.sum(fun[i, j])
            if drho[i, j] > 1e-12:
                ux[i, j] = np.sum([fun[i, j, k] * M[k, 0] for k in range(9)]) / drho[i, j]
                uy[i, j] = np.sum([fun[i, j, k] * M[k, 1] for k in range(9)]) / drho[i, j]
            else:
                ux[i, j] = 0.0
                uy[i, j] = 0.0
    ux[obj] = 0
    uy[obj] = 0
    drho[obj] = 1
    return ux, uy, drho
def equilibrio(x,y,Mat,ux,uy,wh,drho,fun):
    feq = np.zeros((x, y, 9))
    for i in range(x):
        for j in range(y):
            for k in range(9):
                v = Mat[k]
                pp = v[0] * ux[i, j] + v[1] * uy[i, j]
                v2 = ux[i, j]**2 + uy[i, j]**2
                feq[i, j, k] = wh[k] * drho[i, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
                fun[i, j, k] = (1 - w) * fun[i, j, k] + w * feq[i, j, k]
    return fun, feq

def propagacion(x,y,Mat,fun, fun_pre):
    for k in range(9):
        dx, dy = Mat[k]
        for i in range(x):
            for j in range(y):
                ni, nj = i + dx, j + dy
                if 0 <= ni < Nx and 0 <= nj < Ny:
                    fun[ni, nj, k] = fun_pre[i, j, k]
    return fun


def rebote(x,y,obj,fun, fun_pre):
    for i in range(x):
        for j in range(y):
            if obj[i, j]:
                for k in range(9):
                    fun[i, j, k] = fun_pre[i, j, opuestos[k]]
    return fun


def frontera(x,y,ux,uy,drho,fun,wh,Mat):
    for j in range(y):
        ux[0, j] = u0
        uy[0, j] = 0
        drho[0, j] = np.sum(fun[0, j])
        for k in range(9):
            v = Mat[k]
            pp = v[0] * ux[0, j] + v[1] * uy[0, j]
            v2 =ux[0, j]**2 + uy[0, j]**2
            fun[0, j, k] = wh[k] * drho[0, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)

        for k in range(9):
            fun[-1, j, k] = fun[-2, j, k]
    return ux, uy, fun
