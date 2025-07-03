import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt
import random
import imageio #para crear GIFS
import os #manejo de carpetas
#Se hará el primer y segundo paso del algoritmo en Python, que es realizar la red (Matriz) y dar inicio a la densidad y las velocidades
#ctrl + s
N=101

mat_vel=np.zeros((3,3))
mat_den = np.ones((3,3))
# Valores iniciales de los puntos, los bordes de los puntos
print("Densidades", mat_den)
print("Velocidades", mat_vel)

#FUNCION EQUILIBRIO
#iniciamos con los pesos
pesos=np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])
#creamos el for para reccorrer las matrices y llenarlas
f=[]
for i in range(2):
  for j in range(2):
      f[i]=pesos[i]*(mat_den[i,j]+3*np.dot(M[i,j],mat_vel[i,j])-(3/2)*np.dot(mat_vel[i,j],mat_vel[i,j])+(9/2)*(np.dot(M[i,j],mat_vel[i,j]))*(np.dot(M[i,j],mat_vel[i,j])))
#Nos dio error, lo averiguaremos en el proximo avance , continuara...
=======

def inicializar_red(Nx, Ny, vx_inicial=0.1):

    mat_vel = np.zeros((Nx, Ny, 2))
    mat_den = np.ones((Nx, Ny))
    f = np.zeros((Nx, Ny, 9))

    mat_vel[:, :, 0] = vx_inicial

    return mat_vel, mat_den, f
>>>>>>> eaf67fdf9988816846e27315888960aa675f9fb9
