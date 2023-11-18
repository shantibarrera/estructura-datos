"""Se importa el modulo random para generar numeros aleatorios"""
import random
"""Se importa el modulo time para medir el tiempo de ejecucion"""
import time

def bubble_sort(arr):
  """
  Ordena una lista usando el método de burbuja.

  Args:
    arr: La lista a ordenar.

  Returns:
    La lista ordenada.
  """

  n = len(arr)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr







inicio = time.time()
random.seed(10)
buscar = input("Que número desea buscar?")
datos = [random.randint(0, 10000) for _ in range(5000)]
ordenado = buscar_dato(datos, buscar)
print(ordenado)
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)


def buscar_dato(datos):
    
    

if encontrado:
  print(f"El valor {buscar} se encuentra en el arbol")
else:
  print(f"El valor {buscar} no se encuentra en el arbol")