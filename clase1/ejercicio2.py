"""
Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado
"""

class Vehiculo:

    tipo = str
    marca = str
    combustible = str

    def __init__(self, tipo, marca, combustible):
        self.tipo = tipo
        self.marca = marca
        self.combustible = combustible


class Carro(Vehiculo):
    def __init__(self, tipo, marca, combustible):
        super().__init__(tipo, marca, combustible)
        self.tipo = tipo
        self.marca = marca
        self.combustible = combustible

    def __str__(self):
        return f"El carro tipo {self.tipo} de marca {self.marca} usa combustible {self.combustible}"

class Moto(Vehiculo):
    def __init__(self, tipo, marca, combustible):
        super().__init__(tipo, marca, combustible)
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def __str__(self):
        return f"El carro tipo {self.tipo} de marca {self.marca} usa combustible {self.combustible}"

carro = Carro("Carro", "Supra", "Premium")
moto = Moto("Moto", "r6", "Premium")

print(carro)
print(moto)
