# Biblioteca virtual..

# Colocamos la clase Libro y la inicializamos con __init__
class Libro:
    def __init__(self, titulo, autor, catergoria, isbn ):
        self.titulo = titulo
        self.autor = autor # El autor será generado como una tupla
        self.categoria = catergoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} (ISBN: {self.isbn})"

# Asignamos la clase usuario correspondiente al usuario que requiera de los libros
class Usuario:
    def __init__(self, nombre, ID_usuario):
        self.nombre = nombre
        self.ID_usuario = ID_usuario
        self.libros_prestados = []  # ya se asigna aquí

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.ID_usuario}"

# Clase biblioteca correspondiente a la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {} # Colección diccionario (ISBN: libro)
        self.usuarios = {} # ID_usuario: Usuario

# Añadir libro
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print("***LIBRO***")
            print(f"El libro: {libro.titulo} fue añadido.")
            print()
        else:
            print("El libro ya se encuentra en la biblioteca.")

# Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"El libro con ISBN {isbn} fue elimidado.")
        else:
            print("El libro no existe.")

# Registrar usuarios
    def registrar_usuario(self, usuario):
        if usuario.ID_usuario not in self.usuarios:
            self.usuarios[usuario.ID_usuario] = usuario
            print("///USUARIO///")
            print(f"Usuario: {usuario.nombre} registrado.")
            print()
        else:
            print(f"El usuario ya se encuentra registrado.")

# Eliminar usuarios
    def dar_baja_al_usuario(self, ID_usuario):
        if ID_usuario in self.usuarios:
            del self.usuarios[ID_usuario]
            print()
            print("//DADO DE BAJA//")
            print(f"El usuario con ID: {ID_usuario} ha sido eliminado.")
        else:
            print(f"El usuario no se encuentra registrado.")

# Prestar libro
    def prestar_libro(self, ID_usuario, isbn):
        if ID_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return

        if isbn not in self.libros_disponibles:
            print("Libro no disponible.")
            return

        # Analizamos a quien fue prestado el libro

        libro = self.libros_disponibles.pop(isbn)
        self.usuarios[ID_usuario].libros_prestados.append(libro)
        print("###LIBROS PRESTADOS###")
        print(f"El libro: {libro.titulo} fue prestado a {self.usuarios[ID_usuario].nombre}.")

# Devolver libro
    def devolver_libro(self, ID_usuario, isbn):
        if ID_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return

        usuario = self.usuarios[ID_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"El libro: {libro.titulo} ha sido devuelto.")
                return
        print("El usuario no tiene este libro")

    # Buscar libro por autor, titiulo o categoría
    def buscar_libro(self, criterio, valor):
        encontrado = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulado" and valor.lower() in libro.titulo.lower():
                encontrado.append(libro)
            elif criterio == "autor" and (valor.lower() in libro.autor[0].lower() or valor.lower() in libro.autor[1].lower()):
                encontrado.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                encontrado.append(libro)
        return encontrado

    # Lista de libros prestados
    def lista_libros_prestados(self, ID_usuario):
        if ID_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return []
        return self.usuarios[ID_usuario].libros_prestados

def main():

    # instancia de la biblioteca
    instanacia = Biblioteca()

    libro1 = Libro("Cosas de la vida", ("juan", "Mera"), "Vida", "0452")
    libro2 = Libro("Bases de datos", ("Gabriela", "Palacios"), "Tecnología", "73784")
    libro3 = Libro("Herramientas de aprendizaje", ("Fátima", "Romero"), "Educación", "12458")


    # Añadir libros
    instanacia.añadir_libro(libro1)
    instanacia.añadir_libro(libro2)
    instanacia.añadir_libro(libro3)

    # Creación de usuario
    usuario1 = Usuario("Carla Pacheco", "Car788")
    usuario2 = Usuario("Santiago Lara", "San5658")
    usuario3 = Usuario("David Cabezas", "Dav2323")

    # Registrar usuarios
    instanacia.registrar_usuario(usuario1)
    instanacia.registrar_usuario(usuario2)
    instanacia.registrar_usuario(usuario3)

    # Prestar libros
    instanacia.prestar_libro("Car788", "73784")
    instanacia.prestar_libro("San5658", "0452")
    instanacia.prestar_libro("Dav2323", "12458")

    # Lista de libros prestados
    print()
    print("Libros prestados a Carla:")
    print()
    for libro in instanacia.lista_libros_prestados("Car788"):
        print("-", libro)

    # Devolver libro
    instanacia.devolver_libro("Car788", "73784")

    # Buscar libros disponibles por categoría
    print()
    print("Buscar libro por categoria 'Vida': ")
    print()
    resultado = instanacia.buscar_libro("Categoria", "Vida")
    for libro in resultado:
        print("-", libro)

    # Intento de prestar libro
    instanacia.prestar_libro("Dav2323", "73784")

    # Dar de baja al usuario Santiago
    instanacia.dar_baja_al_usuario("San5658")

# Inicializamos el programa
if __name__ == "__main__":
    main()


















