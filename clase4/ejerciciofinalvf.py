# Importa la librería random
import random

# Define una función para generar una lista de nodos aleatorios
def generar_lista_de_nodos(nodos):
    lista_nodos = []
    
    # Genera nodos aleatorios en un rango específico para cada nodo
    for i in range(nodos):
        nodo_minimo = i
        nodo_maximo = i + 50
        nodo_aleatorio = random.randint(nodo_minimo, nodo_maximo)
        lista_nodos.append(nodo_aleatorio)
    
    # Retorna la lista de nodos generada
    return lista_nodos

# Pide al usuario el número de nodos que desea crear
nodos = int(input("Ingrese el número de nodos a crear: "))

# Llama a la función para generar la lista de nodos
lista_final = generar_lista_de_nodos(nodos)

# Imprime la lista con los nodos generados
print("Lista generada:", lista_final)
