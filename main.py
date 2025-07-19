import sys
import os
import imageio
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))

import os
import imageio
from source.Valores_iniciales import inicializar, crear_triangulo, condiciones_frontera
from source.Construccion_algoritmo import colision, propagacion, rebote
from source.Resultados import guardar_imagen
from source.config import Nx, Ny

def main():
    os.makedirs("imagenes_lbm", exist_ok=True)
    imagenes = []
    # Parámetros
    pasos = 1000
    guardar_cada = 10
    fps_gif = 15
    
    # Inicialización
    Obs = crear_triangulo()
    f, rho, vx, vy, Obs = inicializar(Obs)
    imagenes = []
    
    try:
        for t in range(pasos):
            f, rho, vx, vy = colision(f, rho, vx, vy, Obs)
            f = propagacion(f)
            f = rebote(f, Obs)
            f = condiciones_frontera(f, vx, vy, rho)
            
            if t % guardar_cada == 0:
                guardar_imagen(t, vx, vy, Obs, imagenes)
                print(f"Progreso: {t}/{pasos}")
        
        # Crear GIF
        imageio.mimsave("simulacion.gif", imagenes, fps=fps_gif)
    
    finally:
        # Limpieza
        for file in os.listdir("imagenes_lbm"):
            os.remove(f"imagenes_lbm/{file}")
        os.rmdir("imagenes_lbm")

if __name__ == "__main__":
    main()