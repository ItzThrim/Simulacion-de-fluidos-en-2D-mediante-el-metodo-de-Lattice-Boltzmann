import matplotlib.pyplot as plt
import imageio
import numpy as np
import os

def guardar(ux, uy, obj, t, imagenes, carpeta):
    vel = np.sqrt(ux**2 + uy**2)
    vel[obj] = 0
    plt.figure(figsize=(10, 4))
    plt.imshow(vel.T, origin="lower", cmap="magma")
    plt.colorbar(label="Velocidad")
    plt.title(f"Paso {t}")
    nombre = os.path.join(carpeta, f"imagen_{t:04d}.png")
    plt.savefig(nombre)
    plt.close()
    imagenes.append(imageio.imread(nombre))
    print(f"Paso {t} guardado")

