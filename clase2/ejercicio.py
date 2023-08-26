import pandas as pd

archivo = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2013.csv"
df = pd.read_csv (archivo, sep = ";")

class Datos:

    url = ""
    nombre = ""

    def __init__(self, url, nombre):
        self.url = url
        self.nombre = nombre

    def promedio(self, columna):
        return df[columna].mean()

    def suma(self, columna):
        return df[columna].sum()

# Solicitar al usuario la columna a operar
columna_seleccionada = input("Ingrese el nombre de la columna a operar: ")

# Crear una instancia de la clase Datos
mis_datos = Datos(archivo, "Encuesta Cultura 2013")

# Calcular y mostrar el promedio y la suma de la columna seleccionada
if columna_seleccionada in df.columns:
    promedio = mis_datos.promedio(columna_seleccionada)
    suma = mis_datos.suma(columna_seleccionada)
    print(f"Promedio de la columna '{columna_seleccionada}': {promedio:.2f}")
    print(f"Suma de la columna '{columna_seleccionada}': {suma}")
else:
    print("La columna ingresada no existe en el DataFrame.")
