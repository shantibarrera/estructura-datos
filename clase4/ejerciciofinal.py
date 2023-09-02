import random

def lista(nodos):
    lista_final = []
    for i in range(nodos):
        numero_aleatorio = random.randint(i, i + 50)
        lista_final.append(numero_aleatorio)
    return lista_final

nodos = int(input("Ingrese el número de nodos a crear: "))
lista_final = lista(nodos)
print("Lista generada:", lista_final)