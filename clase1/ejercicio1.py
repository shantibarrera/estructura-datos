"""
Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; la también debe contener dos métodos encender y arrancar. 
Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado
"""

class Vehiculo: #se define una clase

    marca = ""
    combustible = ""

    def encender (self):
        return f"Se enciende el vehiculo con combustible {self.combustible}"

    def apagar (self):
        pass

    def __init__(self, combustible, marca):
        self.marca = marca
        self.combustible = combustible

carro = Vehiculo("Premium", "Bugatti")
print (carro.marca)
print ("="*10)
print (carro.encender()) #se imprime por pantalla el resultado final