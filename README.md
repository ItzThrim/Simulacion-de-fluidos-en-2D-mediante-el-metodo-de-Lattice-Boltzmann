# Simulación de Fluidos 2D con el Método de Lattice Boltzmann

Este proyecto implementa una simulación bidimensional de flujo de fluidos utilizando el método de Lattice Boltzmann (LBM). La simulación incluye obstáculos en el dominio, como un triángulo, y permite generar visualizaciones en forma de imágenes y animaciones GIF.

---

## 📁 Estructura del Proyecto


## 🚀 Cómo Ejecutar

1. **Clona o descarga** este repositorio.

2. Asegúrate de tener Python 3 instalado, junto con los siguientes paquetes:

```bash
pip install numpy matplotlib imageio

# Parametros

Nx = 120                # Número de nodos en x
Ny = 60                 # Número de nodos en y
u0 = 0.1                # Velocidad inicial
viscosidad = 0.8        # Viscosidad cinemática
paso_de_tiempo = 500    # Total de pasos temporales
guardar_cada = 10       # Intervalo de guardado de imágenes

##Resultados

