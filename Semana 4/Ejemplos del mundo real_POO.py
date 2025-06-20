# Ejemplos del mundo real devaluación de un celular

# Definimos la clase

class Celular:
    def __init__(self, marca, modelo, procesador, color):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.color = color
        self.costo = 60

    def elevar(self, incrementar):
        # se aumenta el costo del celular
        self.costo += incrementar
        print(f"El celular {self.marca} año {self.modelo} que cuenta con un procesador {self.procesador}, color {self.color}")
        print(f"En el año 2019 aumentó su valor hasta los {self.costo}$")


    def disminuir(self, bajar):
        # Se reduce el costo del celular
        self.costo = max(0, self.costo - bajar)
        print(f"En la actualidad su precio decayó hasta los {self.costo}$")

# Creamos y damos uso de la clase Celular
El_celular = Celular("Motorola", "2019", "Snapdragon 855", "rojo")

#Se hace una suma entre el costo y lo que llego a costar despues se resta con lo que cuesta actualmente

El_celular.elevar(500)
El_celular.disminuir(430)
print()
print(f"El costo actual del celular es de: {El_celular.costo}$")
