# Creación de clases que hagan uso de los metodos __init__ y __del__

# Clase 1 metodo constructor.

print("Ejemplo del rol constructor con el metodo __init__")

# Usamos el metodo __init__ para inicializar el objeto
class Zapatos:
    def __init__(self, talla, color, modelo):
        self.talla = talla
        self.color = color
        self.modelo = modelo

    def Caracteristicas(self):
        return f" Talla: {self.talla}, Color: {self.color}, Modelo: {self.modelo}"

mis_zapatos = Zapatos(41, "Blancos", "Retro")

# Mostramos en pantalla el ejemplo con el constructor y metodo __init__
print(mis_zapatos.Caracteristicas())
print()
print("Ejemplo del rol destructor con el metodo __del__")

# Definimos una nueva clase que nos ayude a iniciar con el metodo __init__
class Camiseta:
    def __init__(self, talla, modelo, marca):
        self.talla = talla
        self.modelo = modelo
        self.marca = marca
        print(f"Camiseta {self.talla}, {self.modelo}, {self.marca} inicializado")

    print()

    # Hacemos uso del metodo __del__ para limpiar o eliminar el amtributo "marca"
    def __del__(self):
        print()
        print("Eliminación de marca por el metodo __del__")
        print()
        print (f"Camiseta {self.talla}, {self.modelo} liberado")

mi_camiseta = Camiseta("M", "Polo", "Nike")
del mi_camiseta


