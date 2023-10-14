class ItemCompra:
    def __init__(self, libro, cantidad: int):
        self.libro = libro 
        self.cantidad = cantidad

    def calcular_subtotal(self):
        subtotal = self.cantidad * self.libro.precio 
        return subtotal