#Importa la libreria random
import random

def lista(nodos): #Crea una función para la lista de nodos
    lista_final = []
    for i in range(nodos): #Crea un condicional dependiendo de los nodos que quiera crear el usuario
        numero_aleatorio = random.randint(i, i + 20) #Inserta un número aleatorio con la función random.randint entre i e i + 10
        lista_final.append(numero_aleatorio)
    return lista_final  #Nos retorna la lista con los nodos creados

nodos = int(input("Ingrese el número de nodos a crear: ")) #Se le pide al usuario el número de nodos que desea crear
lista_final = lista(nodos)

print("Lista generada:", lista_final) #Imprime la lista con los nodos generados