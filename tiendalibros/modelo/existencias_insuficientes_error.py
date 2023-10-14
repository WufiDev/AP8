from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    # Defina metodo inicializador
    def __init__(self, LibroError, cantidad_a_comprar:int, titulo, isbn, existencias):
        self.LibroError = LibroError
        self.cantidad_a_comprar = cantidad_a_comprar
        self.titulo = titulo
        self.isbn = isbn
        self.existencias = existencias
    # Defina metodo espcial
    def __str__(self):
        return (f"El libro con título {self.titulo} y ISBN {self.isbn} no tiene suficientes existencias para realizar la compra: "
                f"cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}")