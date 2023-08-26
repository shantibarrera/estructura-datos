"""
Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender,
se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debajo de un 10%,
si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 
"""

class Vehiculo:
    def __init__(self, tipo, marca, combustible):
        self.tipo = tipo
        self.combustible = combustible
        self.marca = marca

class Carro(Vehiculo):
    def __init__(self, tipo, marca, combustible):
        super().__init__(tipo, marca, combustible)
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def encender(self):
        if self.combustible >= 10:
            print(f"El {self.tipo} se ha encendido.")
        else:
            print(f"Advertencia: El {self.tipo} necesita ir a la gasolinera. Para poder encender debe tener más de 10%")

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible} galones"

class Moto(Vehiculo):
    def __init__(self, marca, tipo, combustible):
        super().__init__(tipo, marca, combustible)
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def encender(self):
        if self.combustible >= 10:
            print(f"La {self.tipo} se ha encendido.")
        else:
            print(f"Advertencia: La {self.tipo} necesita ir a la gasolinera.")

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible} galones"

# Crear instancias de las clases
carro = Carro("Carro", "McClaren", 9)
moto = Moto("Moto", "H2R", 14)

# Intentar encender los vehículos
carro.encender()
moto.encender()
