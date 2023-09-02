import random

class Nodo:
    dato = None
    apuntador = None
    def __init__(self, dato, apuntador):
        self.dato = dato 
        self.apuntador = apuntador

    def __str__(self):  
        return f"{self.dato}"
    
def lista_nodos(n):
    if n == 0:
        return [n]
    else:
        return lista_nodos
    
def lista_random(n):
    lista = [n] * n
    for i in range (n):
        lista[i] = random.random()
    return lista

n = input("Digite el número de nodos que desea crear: ")
print(lista_nodos(4))
aleatorios = lista_random(n)
print(aleatorios)






