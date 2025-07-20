import imageio
import os

def crear_gif(desde_carpeta, nombre_gif='Lattice.gif'):

    archivos = sorted([
        os.path.join(desde_carpeta, f) 
        for f in os.listdir(desde_carpeta) 
        if f.endswith(('.png', '.jpg', '.jpeg'))
    ])

    imagenes = [imageio.imread(f) for f in archivos]

    # Guardar el gif
    imageio.mimsave(nombre_gif, imagenes, fps=10)
    print(f"GIF guardado como {nombre_gif}")