# Técnicas de programación.

# Personajes de futbol.

# ABSTRACCIÓN: colocar los atributos necesarios

# ENCAPSULACIÓN: como podemos ver este metodo es para impedir que sean accesibles desde fuera y se usa
# doble guión bajo __ esto no permitira acceder a la información si no se colocan. (Este punto no es
# necesario pero si importante conocer) ya que se puede seguir accediendo a los atributos si los llamamos.

print()

print("//////////// CONOCE A TU JUGADOR Y ESCOGE AL MEJOR ////////////////")

print()

# DESTINAMOS ATRIBUTOS

class Personaje:

     def __init__(self, nombre, fuerza, inteligencia, regate, tiro, resistencia, defensa):
         self.nombre = nombre
         self.__fuerza = fuerza
         self.inteligencia = inteligencia
         self.regate = regate
         self.tiro = tiro
         self.resistencia = resistencia
         self.defensa = defensa

    # Encapsulación

     def get_fuerza(self):
         return self.__fuerza

# IMPRIMIMOS LOS ATRIBUTOS

     def atributos(self):
         print(self.nombre, sep= "")
         print("Fuerza:", self.__fuerza)
         print("Inteligencia: ", self.inteligencia)
         print("Regate:", self.regate)
         print("Tiro:", self.tiro)
         print("Resistencia:", self.resistencia)
         print("Defensa:", self.defensa)

# INCREMENTAMOS LOS ATRIBUTOS

     def subir_nivel(self, fuerza, inteligencia, regate, tiro, resistencia, defensa):
         self.__fuerza = self.__fuerza + fuerza
         self.inteligencia = self.inteligencia + inteligencia
         self.regate = self.regate + regate
         self.tiro = self.tiro + tiro
         self.resistencia = self.resistencia + resistencia
         self.defensa = self.defensa + defensa

     def can(self):
         return self.resistencia > 0


     def cansado(self):
         self.resistencia = 0
         print(self.nombre, "Ha llegado a su limite el jugador")

     def obt_fuerza(self):
         return self.__fuerza

# DESTINAMOS UN ADVERSARIO QUE INTERVIENE EL REGATE DE EL PERSONAJE PRINCIPAL CON EL SECUNDARIO

     def superar(self, defe):
         return self.regate - defe.defensa

# IMPRIMIMOS LOS ATRIBUTOS SIN MEJORAR

print("SIN ENTRENAMIENTO")
mi_presonaje = Personaje("Jonathan", 99, 99, 99, 90, 60, 20)
mi_presonaje.atributos()

print()

# IMPRIMIMOS LOS ATRIBUTOS MEJORADOS ASIGNANDO PUNTOS EN ELLOS

print("CON ENTRENAMIENTO")
mi_presonaje.subir_nivel(1, 3, 2, 1, 7, 1)
mi_presonaje.atributos()

print()
# DESTINAMOS LAS HABILIDADES DEL PERSONAJE SECUNDARIO

print("Defensa contrario")
mi_defe = Personaje("Josue", 88, 77, 60, 90, 90, 80)
mi_defe.atributos()

print()

print("Por cada regate de Jonathan baja la defensa de Josue : ")
print(mi_presonaje.superar(mi_defe), "puntos")

print()

# HERENCIA
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print()

print("Hermano de Jonathan: David")

print()

class hermano(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, regate, tiro, resistencia, defensa, cabeceo):
        super().__init__(nombre, fuerza, inteligencia, regate, tiro, resistencia, defensa)
        self.cabeceo = cabeceo

# Metodo que seleccione zapatos deportivos

    def cambiar_zapatos(self):
        opcion = int(input("Elije un par de zapatos para destinar la capacidad de tiro de David: (1) NIKE, (2) PUMA, (3) ADIDAS: "))
        print()
        if opcion == 1:
            self.tiro = 30
        elif opcion == 2:
            self.tiro = 50
        elif opcion == 3:
            self.tiro = 80

        else:
            print("Número introducido incorrecto, por lo tanto se escogera uno estandar")

        print()

# Herencia

David = hermano("David", 100, 99, 99, 60, 70, 100, 140)
David.cambiar_zapatos()
David.atributos()
print("Cabeceo:", David.cabeceo)

def supera(self, reg):
    return self.regate - reg.defensa

print()

print("Por cada regate de Jonathan la defensa de David baja : ")

print(mi_presonaje.superar(David), "puntos")

# POLIMORFISMO

print()

class jugador_jonathan():
    def posicion(self):
        print("Soy delantero", "tengo 17años", "soy goleador")

class jugador_david():
    def posicion(self):
        print("soy defensa", "tengo 21 años", "soy un gran muro")

def posicion_jugador(pos):
    pos.posicion()

print("////////////////////////////////////////////////////////////////////////////////")

print("Despues de haber conocido a Jonathan y David es hora de que escojas a tu jugador")

print("|| Jonatan ||")
posicion_jugador(jugador_jonathan())
print("|| David ||")
posicion_jugador(jugador_david())
print()
# Obtención de fuerza por encapsulación
print(mi_presonaje.obt_fuerza())


