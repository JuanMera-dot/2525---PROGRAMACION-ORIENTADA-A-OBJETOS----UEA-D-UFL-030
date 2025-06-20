# Asignación de carro segun su tipo de licencia
# Creamos la clase Auto

class Auto:
    def __init__(self, tipo, año):
        self.tipo = tipo
        self.año = año
        self.conductor = None

# Creamos una funcion que nos ayude asignar un conductor

    def asignación_conductor(self, persona):
        if isinstance(persona, Persona):
            self.conductor = persona

# Se usa el metodo especial str para la representación en cadena del objeto
    def __str__(self):
        return f"Auto {self.tipo} del año {self.año} va ha ser conducido por: {self.conductor.nombre if self.conductor else "¡¡hasta ahora no hay conductor!!"}."

# Creamos la clase persona para asignar un nombre y una licencia

class Persona:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia


    def __str__(self):
        return f"Señor {self.nombre} con licencia tipo {self.licencia}"

#Creamos y damos uso de la clase Auto y Persona
auto_uno = Auto("pesado-Hino", 2020)
auto_dos = Auto("liviano-Toyota", 2024)
Conductor = Persona("Juan", "E")


auto_uno.asignación_conductor(Conductor)

# Imprimimos todo en pantalla
print(auto_uno)
print(auto_dos)
print(Conductor)


