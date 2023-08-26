"""
La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro o Moto -),
esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto y al momento de imprimir el objeto
debe indicar el tipo de vehiculo junto con el texto mostrado anteriormente 
"""

class Vehiculo:

    tipo = str
    marca = str
    combustible = str

    def __init__(self, tipo, marca, combustible):
        self.tipo = tipo
        self.marca = marca
        self.combustible = combustible

    def mostrar_info(self):
        print(f"Este es un {self.tipo} marca {self.marca} y usa gasolina {self.combustible}")
    

class Carro(Vehiculo):

    def __init__(self, tipo, marca, combustible):
        super().__init__(tipo, marca, combustible)
        self.tipo = "Carro"

class Moto(Vehiculo):

    def __init__(self, tipo, marca, combustible):
        super().__init__(tipo, marca, combustible)
        self.tipo = "Moto"

carro = Carro("Carro", "Buggati", "Extra")
moto = Moto("Moto", "Suzuki", "Corriente")

carro.mostrar_info()
moto.mostrar_info()
