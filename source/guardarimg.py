import matplotlib.pyplot as plt
import imageio
import numpy as np
import os

def guardar(ux, uy, obj, t, imagenes, carpeta, imagenes_densidad, drho, carpeta_den):
    """
    Guarda las imágenes de velocidad y densidad en las carpetas
    
    """
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
        
    # Aca soloc opie y pegue lo de arriba no me reganen
    plt.figure(figsize=(10, 4))
    plt.imshow(drho.T, origin="lower", cmap="viridis")
    plt.colorbar(label="Densidad")
    plt.title(f"Densidad - Paso {t}")
    nombre_rho = os.path.join(carpeta_den, f"imagen_{t:04d}.png")
    plt.savefig(nombre_rho)
    plt.close()
    imagenes_densidad.append(imageio.imread(nombre_rho))

    
    print(f"Paso {t} guardado")