import folium

# Coordenadas para la proyección única del catastro
lat, lon = 6.2461906, -75.5608901  # Latitud y longitud de Nueva York (ejemplo)

# Crear un mapa centrado en las coordenadas dadas
mapa = folium.Map(location=[lat, lon], zoom_start=12)

# Añadir un marcador en la ubicación específica
folium.Marker([lat, lon], popup='Ubicación del catastro').add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save('proyeccion_catastro.html')
