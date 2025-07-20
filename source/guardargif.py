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

def crear_gif(nombre_salida, imagenes):
    try:
        with imageio.get_writer(nombre_salida, mode='I', duration=0.1) as writer:
            for imagen in imagenes:
                writer.append_data(imageio.imread(imagen))
        print(f"GIF guardado correctamente como '{nombre_salida}'")
    except Exception as e:
        print(f"Error al crear el GIF: {e}")