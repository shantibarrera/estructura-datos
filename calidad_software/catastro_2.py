import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium

# Simulación de datos para la evaluación del catastro
np.random.seed(0)
lat = np.random.uniform(6, 7, 100)
lon = np.random.uniform(-75, -76, 100)

# Evaluación de la confiabilidad
confiabilidad = np.mean(lat) / np.std(lat)

# Creación del mapa de proyección única para el catastro
mapa = folium.Map(location=[np.mean(lat), np.mean(lon)], zoom_start=10)

# Añadir marcadores al mapa
for la, lo in zip(lat, lon):
    folium.Marker([la, lo], popup='Punto de Catastro', icon=folium.Icon(color='blue')).add_to(mapa)

# Guardar el mapa como archivo HTML
mapa.save('proyeccion_catastro.html')

# Resultados
print(f"Confiabilidad de la proyección del catastro: {confiabilidad}")