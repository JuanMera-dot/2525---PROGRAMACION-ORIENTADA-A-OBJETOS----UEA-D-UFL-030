#Aplicar los conocimientos adquiridos sobre Definición de Clase, Definición de Objeto, Herencia, Encapsulación y Polimorfismo
# en Python para desarrollar un programa.
# Definir la clase base

class Telefono:
    def __init__(self, marca, modelo, procesador, almacenamiento):
        self.__marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.almacenamiento = almacenamiento

    # Aplicamos encapsulamiento al atributo "marca"
    def get_marca(self):
        return self.__marca

    def descripcion(self):
        return f"El telefono de marca {self.__marca}, modelo {self.modelo}, con procesador {self.procesador}"

# Demostrar el concepto de herencia a traves de una clase derivada

class Atributos(Telefono):
    def __init__(self, marca, modelo, procesador, almacenamiento, carga_rapida, pantalla):
        super().__init__(marca, modelo, procesador, almacenamiento)
        self.carga_rapida = carga_rapida
        self.pantalla = pantalla

    def mostrar_informacion(self):
        return (f"El telefono {self.get_marca()} Año {self.modelo} cuenta con un procesador {self.procesador}"
                f" y un almacenamiento de {self.almacenamiento}Gb, ahora tambien incluye una carga rapida de {self.carga_rapida}w"
                f" con un tipo de mantalla {self.pantalla}")


# Polimorfismo por sobreescritura del metodo descripcion()
    def descripcion(self):
        return (f"El telefono {self.get_marca()} Año {self.modelo} cuenta con un procesador {self.procesador}"
                f" y un almacenamiento de {self.almacenamiento}Gb, ahora tambien incluye una carga rapida de {self.carga_rapida}w"
                f" con un tipo de mantalla {self.pantalla}")


# Clase base

print("/// Telefono base, sin herencia ///")

telefono_base = Telefono("Infinix", 2024, "Helio g100", 266)
print(telefono_base.descripcion())

print()

# Creacion de objetos por polimorfismo

print("/// Polimorfismo por sobreescritura ///")

telefono_uno = Telefono("Samsung", 2023, "Helio g88", 128)
telefono_dos = Atributos("Xiaomi", 2023, "Snapdragon", 256, 20, "Amoled")
print(telefono_uno.descripcion())
print(telefono_dos.mostrar_informacion())

print()

print("/// Con herencia ///")
telefono_en_venta = Atributos("Infinix", 2024, "Helio g100", 256, 18, "Amoled")
print(telefono_en_venta.mostrar_informacion())


