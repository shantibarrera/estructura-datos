class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)

print("Lista original:")
lista.mostrar()

dato_a_eliminar = 2
if lista.eliminar(dato_a_eliminar):
    print(f"Se eliminó el nodo con el dato {dato_a_eliminar}")
else:
    print(f"No se encontró un nodo con el dato {dato_a_eliminar}")

print("Lista después de eliminar el nodo:")
lista.mostrar()
