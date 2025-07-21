import numpy as np
import sys
import os
import imageio
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))
from source.parametros import *
from source.algoritmo import *
from source.obstaculo import *
from source.guardarimg import guardar
from gif import crear_gif

script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_imagenes = os.path.join(script_dir, "imagenes_lbm")
os.makedirs(ruta_imagenes, exist_ok=True)

script_dir = os.path.dirname(os.path.abspath(__file__))
ruta_imagenes_den = os.path.join(script_dir, "imagenesden_lbm")
os.makedirs(ruta_imagenes_den, exist_ok=True)

#Definimos los espacios de velocidad, densidad y la función a trabajar

f = np.zeros((Nx, Ny, 9))
rho = np.ones((Nx, Ny))
vx = np.zeros((Nx, Ny))
vy = np.zeros((Nx, Ny))

#añadimos el array de imagenes para crear el gif luego

imagenes = []
imagenes_den = []


#Creamos el flujo inicial que surge de manera constante desde el lado izquierdo

f, vx, vy = flujo(Nx,Ny,vx,vy,M,f,u0,pesos,rho)

#aca definimos el objeto deseado y sus caracteristicas

#Obs = crear_obstaculo_circulo(Nx//2, Ny//2, 20)
#Obs = crear_obstaculo_triangulo(10, 10, 20, 30, 30, 10)
#Obs = crear_obstaculo_rectangulo(10, 10, 20, 30)
Obs = crear_obstaculo_vaca(int(Nx/2), int(Ny/2))
#Obs = crear_obstaculo_vacio(Nx, Ny)

#Iniciamos el algoritmo a través del tiempo

for t in range(paso_de_tiempo):

    #iniciamos con la funcion de colision

    vx, vy, rho = colision(Nx, Ny, rho, vx, vy, Obs,f)

    #equilibramos la funcion de colision

    f, f_eq = equilibrio(Nx, Ny, M, vx, vy, pesos, rho, f)

    #guardar los valores pre-colisión y poder actualizarlos sin interferencia
    #aqui habia un error en nuestro codigo haciamos fpropagacion=f eso significa que dos archivos apuntan al mismo array
    #y combinaban los resultados lo que es icorrecto

    fun_pre = np.copy(f)

    f = propagacion(Nx, Ny, M, f, fun_pre)

    #Interaccion del fluido con el objeto

    f = rebote(Nx, Ny, Obs, f, fun_pre)

    #definimos las ocndiciones de frontera para el flujo

    vx, vy, f = frontera(Nx, Ny, vx, vy, rho, f, pesos, M)

    #Guardamos las imagenes de densidad y velocidady realizamos los gifs correspondientes

    if t % guardar_cada == 0:
        guardar(vx, vy, Obs, t,imagenes,ruta_imagenes, imagenes_den, rho, ruta_imagenes_den)

crear_gif(ruta_imagenes, "ejemplo_vaca_lbm.gif", ruta_imagenes_den, "ejemplo_vaca_lbm_densidad.gif")