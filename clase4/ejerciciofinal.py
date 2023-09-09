#Importa la libreria random
import random

#Crea una función para la lista de nodos
def lista(nodos):
    lista_final = []
    #Crea un condicional dependiendo de los nodos que quiera crear el usuario
    for i in range(nodos):
        #Inserta un número aleatorio con la función random.randint entre i e i + 10
        numero_aleatorio = random.randint(i, i + 50)
        lista_final.append(numero_aleatorio)
    #Nos retorna la lista con los nodos creados
    return lista_final

#Se le pide al usuario el número de nodos que desea crear
nodos = int(input("Ingrese el número de nodos a crear: "))
lista_final = lista(nodos)

#Imprime la lista con los nodos generados
print("Lista generada:", lista_final)