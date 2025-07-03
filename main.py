import sys
import os

sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("initpy"))

import numpy as np
from Valores_iniciales import inicializar_red
from Construccion_algoritmo import actualizar_equilibrio_global, colisionar, propagar, recalcular_macros

Nx, Ny = 3, 3
mat_vel, mat_den, f = inicializar_red(Nx, Ny)

f = actualizar_equilibrio_global(f, mat_den, mat_vel)

fcol = colisionar(f, w=2)

fprop = propagar(fcol)

mat_den, mat_vel = recalcular_macros(fprop)

f = actualizar_equilibrio_global(f, mat_den, mat_vel)

print("Densidad en (0,0):", mat_den[0, 0])
print("Velocidad en (0,0):", mat_vel[0, 0])
