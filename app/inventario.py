class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        if nombre in self.productos:
            self.productos[nombre] += cantidad
        else:
            self.productos[nombre] = cantidad
        return self.productos[nombre]

    def obtener_stock(self, nombre):
        return self.productos.get(nombre, 0)
    
    def vaciar_inventario(self):
        self.productos = {}
        return True