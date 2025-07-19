# simulacion_lb.py
import os
import numpy as np
import matplotlib.pyplot as plt
import imageio

def guardar_imagen(t, vx, vy, Obs, imagenes):
    vel = np.sqrt(vx**2 + vy**2)
    vel[Obs] = 0
    plt.figure(figsize=(10, 4))
    plt.imshow(vel.T, origin="lower", cmap="magma")
    plt.colorbar(label="Velocidad")
    plt.title(f"Paso {t}")
    nombre = f"imagenes_lbm/imagen_{t:04d}.png"
    plt.savefig(nombre)
    plt.close()
    imagenes.append(imageio.imread(nombre))
