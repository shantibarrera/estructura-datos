"""
Debes hacer un ejercicio donde por medio de un método, el vehículo de marcha y haga un consumo de combustible a medida que este funcione,
cuando llegue a los niveles de combustible definidos en el mensaje anterior, muestre la advertencia y si esta llega a cero, detenga la marcha 
Solución: solución 5 - Plantea tu propia solución y comparte la en clase
"""
class Vehiculo:
    def __init__(self, tipo, marca, combustible):
        self.tipo = tipo
        self.combustible = combustible
        self.marca = marca
        self.encendido = False

    def encender(self):
        if self.combustible >= 10:
            self.encendido = True
            print(f"El {self.tipo} se ha encendido.")
        else:
            print(f"Advertencia: El {self.tipo} necesita ir a la gasolinera. Debe tener minimo un 10% para arrancar.")

    def apagar(self):
        self.encendido = False
        print(f"El {self.tipo} se ha apagado.")

    def avanzar(self, distancia):
        if self.encendido:
            consumo = distancia * 0.50  # Consumo estimado por distancia
            if self.combustible > consumo:
                self.combustible -= consumo
                print(f"{self.tipo} avanzó {distancia} unidades. Combustible restante: {self.combustible:.2f} galones")
                if self.combustible < 5: #Unidades que salta para avanzar el carro
                    print(f"Advertencia: El {self.tipo} necesita ir a la gasolinera.")
                if self.combustible <= 0:
                    self.apagar()
                    print(f"Deteniendo el {self.tipo} debido a falta de combustible.")
            else:
                print(f"El {self.tipo} no tiene suficiente combustible para avanzar.")
        else:
            print(f"El {self.tipo} está apagado, enciéndelo primero.")

class Carro(Vehiculo):
    def __init__(self, marca, tipo, combustible):
        super().__init__(tipo, marca, combustible)
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible:.2f} galones"

class Moto(Vehiculo):
    def __init__(self, marca, tipo, combustible):
        super().__init__(tipo, marca, combustible)
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def __str__(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible:.2f} galones"

# Crear instancias de las clases
# Se define el tipo de vehiculo, la marca del vehiculo y la cantidad de gasolina en galones
carro = Carro("Carro", "Spark", 30) 
moto = Moto("Moto", "Boxer", 9)

# Encender los vehículos
carro.encender()
moto.encender()

# Avanzar los vehículos
carro.avanzar(10)
moto.avanzar(5)

# Consumir más combustible para llegar a la advertencia
carro.avanzar(15)
moto.avanzar(10)

# Consumir todo el combustible
carro.avanzar(30)
moto.avanzar(20)
