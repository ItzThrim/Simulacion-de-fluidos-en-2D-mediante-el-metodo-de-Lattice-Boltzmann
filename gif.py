import imageio
import os


def crear_gif(desde_carpeta, nombre_gif='Lattice.gif', desde_carpeta_den=None, nombre_gif_den='Lattice_densidad.gif'):

    """
    Funcion destinada a crear los gifs de velocidad y densidad con las imagenes generadas 
    en la funcion de crear imagenes.
    """
    # Crear primer gif desde carpeta de velocidad u otra magnitud
    archivos = sorted([
        os.path.join(desde_carpeta, f) 
        for f in os.listdir(desde_carpeta) 
        if f.endswith(('.png', '.jpg', '.jpeg'))
    ])
    imagenes = [imageio.imread(f) for f in archivos]
    imageio.mimsave(nombre_gif, imagenes, fps=10)
    print(f"GIF guardado como {nombre_gif}")

    # Crear segundo gif desde carpeta de densidad (si se proporciona)
    if desde_carpeta_den is not None:
        archivosden = sorted([
            os.path.join(desde_carpeta_den, j) 
            for j in os.listdir(desde_carpeta_den) 
            if j.endswith(('.png', '.jpg', '.jpeg'))
        ])
        imagenesden = [imageio.imread(j) for j in archivosden]
        imageio.mimsave(nombre_gif_den, imagenesden, fps=10)
        print(f"GIF guardado como {nombre_gif_den}")