from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    # Defina metodo inicializador
    def __init__(self, LibroError):
        self.LibroError = LibroError
    # Defina metodo especial
    def __str__(self, titulo, isbn):
        super().__init__(f"El libro con título {titulo} y ISBN: {isbn} ya existe en el catálogo.")
        self.titulo = titulo
        self.isbn = isbn
        return f"El libro con título {self.titulo} y ISBN: {self.isbn} ya existe en el catálogo"
