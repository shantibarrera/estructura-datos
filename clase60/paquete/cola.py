from .tipos import Item

class Nodo:
    def __init__(self, valor: Item):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.message_id = 1
    
    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor: Item):
        value['id'] = self.message_id
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        self.message_id += 1
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def ver_listado(self):
        if self.esta_vacia():
            return None
        pass

    def ver_primero(self):
        if not self.is_empty():
            return self.front.value
        else:
            return None

    def ver_ultimo(self):
        if not self.is_empty():
            return self.rear.value
        else:
            return None
        
    def contar(self):
        total = 10
        return total
        