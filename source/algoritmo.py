import numpy as np
from parametros import Nx, Ny, u0, viscosidad, tau, w, paso_de_tiempo, guardar_cada, M, pesos, opuestos



def flujo(x,y,ux,uy,Mat,fun,v0,wh,drho):

  """Inicializa el flujo imponiendo una velocidad constante v0 en el borde izquierdo.
  Calcula la función de distribución de equilibrio `fun` en función de `ux`, `uy` y `drho`.
  """

# Flujo constante en izquierda Condición inicial
  for i in range(x):
      for j in range(y):
          if i < 10:
            # Inicia el flujo desde la izquierda con una velocidad v0
            ux[i, j] = v0
              #vx[-i,j] = -u0
          for k in range(9):
              v = Mat[k]
              pp = v[0] * ux[i, j] + v[1] * uy[i, j]
              v2 = ux[i, j]**2 + uy[i, j]**2
              # funcion de la distribucion de equilibrio
              fun[i, j, k] = wh[k] * drho[i, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
  return fun, ux, uy



def colision(x,y,drho,ux,uy,obj,fun):
    """Calcula la densidad y las velocidades (ux, uy) a partir de la función de distribución `fun`.
    Aplica condiciones de no deslizamiento en las celdas del obstáculo.
    """
    for i in range(x):
        for j in range(y):
            # caclula la densidad local com osuma de las funs de distribucion
            # normalizamos la velocidad en valor de la densidad
            drho[i, j] = np.sum(fun[i, j])
            if drho[i, j] > 1e-12:
                ux[i, j] = np.sum([fun[i, j, k] * M[k, 0] for k in range(9)]) / drho[i, j]
                uy[i, j] = np.sum([fun[i, j, k] * M[k, 1] for k in range(9)]) / drho[i, j]
            else:
                ux[i, j] = 0.0
                uy[i, j] = 0.0

# Definimos las considoines en el objeto, luego toca definir el rebote, si no vuelve a fallar y superamos la velcoidad de la luz
    ux[obj] = 0
    uy[obj] = 0
    drho[obj] = 1
    return ux, uy, drho
def equilibrio(x,y,Mat,ux,uy,wh,drho,fun):

    """Calcula la función de distribución de equilibrio `feq` y actualiza `fun`
    mediante el esquema de colisión.
    """

    feq = np.zeros((x, y, 9))
    for i in range(x):
        for j in range(y):
            for k in range(9):
                v = Mat[k]
                pp = v[0] * ux[i, j] + v[1] * uy[i, j]
                v2 = ux[i, j]**2 + uy[i, j]**2
                feq[i, j, k] = wh[k] * drho[i, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)
    # Actualiza la función de trabajo y la de equilirbio
                fun[i, j, k] = (1 - w) * fun[i, j, k] + w * feq[i, j, k]
    return fun, feq

def propagacion(x,y,Mat,fun, fun_pre):
    """Realiza la propagacoin de la función de distribución fun_pre
    a través de la red de velocidades, actualizando fun.
    """
    for k in range(9):
        dx, dy = Mat[k]
        for i in range(x):
            for j in range(y):
                ni, nj = i + dx, j + dy
                # Verifica la posicion vecina y se asegura de que no se salga del dominio
                if 0 <= ni < Nx and 0 <= nj < Ny:
                    # Porpaga la funcion a la posicon de al lado
                    fun[ni, nj, k] = fun_pre[i, j, k]
    return fun


def rebote(x,y,obj,fun, fun_pre):

    """Aplica la condición de rebote en las celdas marcadas como obstáculos.
    Invierte la dirección de las partículas que colisionan con los obstáculos.
    """
    # Aca casi nos morimos ocn la condicion de rebote, cambiamos la direccion a la opuesta
    for i in range(x):
        for j in range(y):
            if obj[i, j]:
                for k in range(9):
                    # invertimos las direcciones de las particulas
                    fun[i, j, k] = fun_pre[i, j, opuestos[k]]
    return fun


def frontera(x,y,ux,uy,drho,fun,wh,Mat):

    """Impone condiciones de frontera:
    Entrada izquierda: velocidad fija `u0` y densidad calculada.
    Salida derecha: condición de salida libre (valores copiados).
    """

#Impone condiciones de frontera en los laterales

    for j in range(y):
        # Borde izquierdo
        ux[0, j] = u0
        uy[0, j] = 0
        drho[0, j] = np.sum(fun[0, j])
        for k in range(9):
            v = Mat[k]
            pp = v[0] * ux[0, j] + v[1] * uy[0, j]
            v2 =ux[0, j]**2 + uy[0, j]**2
            # recalcula la funcion de distribucion en la entrada
            fun[0, j, k] = wh[k] * drho[0, j] * (1 + 3*pp + 4.5*pp**2 - 1.5*v2)

    # Borde derecho da las condiciones de salida y evita que regrese

        for k in range(9):
            fun[-1, j, k] = fun[-2, j, k]
    return ux, uy, fun
