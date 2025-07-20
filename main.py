import numpy as np
import sys
import os
import imageio
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))
from source.parametros import *
from source.algoritmo import *
from source.obstaculo import crear_obstaculo_triangulo, crear_obstaculo_circulo, crear_obstaculo_rectangulo, crear_obstaculo_vaca
from source.guardarimg import guardar
from gif import crear_gif

script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_imagenes = os.path.join(script_dir, "imagenes_lbm")
os.makedirs(ruta_imagenes, exist_ok=True)

f = np.zeros((Nx, Ny, 9))
rho = np.ones((Nx, Ny))
vx = np.zeros((Nx, Ny))
vy = np.zeros((Nx, Ny))
imagenes = []


f, vx, vy = flujo(Nx,Ny,vx,vy,M,f,u0,pesos,rho)

#Obs = crear_obstaculo_circulo(Nx//2, Ny//2, 20)
#Obs = crear_obstaculo_triangulo(10, 10, 20, 30, 30, 10)
#Obs = crear_obstaculo_rectangulo(10, 10, 20, 30)
Obs = crear_obstaculo_vaca(int(Nx/2), int(Ny/2))


for t in range(paso_de_tiempo):
    vx, vy, rho = colision(Nx, Ny, rho, vx, vy, Obs,f)

    f, f_eq = equilibrio(Nx, Ny, M, vx, vy, pesos, rho, f)

    fun_pre = np.copy(f)

    f = propagacion(Nx, Ny, M, f, fun_pre)
    f = rebote(Nx, Ny, Obs, f, fun_pre)
    vx, vy, f = frontera(Nx, Ny, vx, vy, rho, f, pesos, M)

    if t % guardar_cada == 0:
        guardar(vx, vy, Obs, t,imagenes,ruta_imagenes)

crear_gif(ruta_imagenes, "ejemplo_vaca_lbm.gif")