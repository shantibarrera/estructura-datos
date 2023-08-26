edades = [11, 21, 23, 35, 45]

def promedio_edades(edades):
    suma = 0
    for i in edades:
        suma = suma + i
    return suma / len(edades)

promedio = promedio_edades(edades)

print(f"El promedio de edades es: {promedio}")

for i in edades:
    print (f"Edad:  {i}")