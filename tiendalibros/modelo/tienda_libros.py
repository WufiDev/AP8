class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self, catalogo, carrito, isbn, CarroCompras):
        self.catalogo = {isbn}
        self.carrito = CarroCompras()

    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn:str, titulo:str, precio:float,existencias:int):
        if isbn in self.catálogo:
            raise LibroExistenteError(titulo, isbn)
        nuevo_libro = Libro(titulo, isbn, precio, existencias)
        self.catálogo[isbn] = nuevo_libro
        return nuevo_libro
    
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro not in self.catálogo:
            raise ValueError("El libro no existe en el catálogo.")  

        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)

        self.carrito.agregar_item(libro, cantidad)

    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)