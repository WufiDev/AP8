class CarroCompras:
    # Defina metodo inicializador __init__(self)
    def __init__(self):
        self.item = []
    # Defina el metodo agregar_item
    def agregar_item(self, libro, cantidad):
        nuevo_item = itemcompra(libro,cantidad)
        self.items.append(self.item)
        return nuevo_item
    # Defina el metodo calcular_total
    def calcular_total(self):
        total= 0.0
        for item in self.item:
            subtotal = item.calcular_subtotal()
            total += subtotal
        return total 
    # Defina el metodo quitar_item
    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]