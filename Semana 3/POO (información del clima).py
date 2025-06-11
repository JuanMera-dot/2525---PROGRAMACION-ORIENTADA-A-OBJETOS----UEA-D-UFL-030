# Promedio semanal del clima.

# Definimos las clases

class diario:

    def __init__(self, temperatura):
        self.temperatura = temperatura

# Definimos para otra clase para almacenar el clima diario

class semana_tem:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, temperatura):
        clima_al_dia = diario(temperatura)
        self.dias.append(clima_al_dia)

# Realizamos la operacion para calcular el promedio del clima durante la semana

    def prom(self):
        total = sum(dia.temperatura for dia in self.dias)
        return total / len(self.dias) if self.dias else 0


def ma():
    sem = semana_tem()
    print("Ingresa la temperatura de cada dia de la semana: ")
    print()

# Usamos un bucle for con la idea de preguntar en cada dia de la semana la temperatura

    for i in range(1):
        tiem = float(input(f"lunes: {i + 1}: "))
        sem.agregar_dia(tiem)

    for i in range(1):
        tiem = float(input(f"martes: {i + 1}: "))
        sem.agregar_dia(tiem)

    for i in range(1):
        tiem = float(input(f"miercoles: {i + 1}: "))
        sem.agregar_dia(tiem)

    for i in range(1):
        tiem = float(input(f"jueves: {i + 1}: "))
        sem.agregar_dia(tiem)

    for i in range(1):
        tiem = float(input(f"viernes: {i + 1}: "))
        sem.agregar_dia(tiem)

    for i in range(1):
        tiem = float(input(f"sabado: {i + 1}: "))
        sem.agregar_dia(tiem)

    for i in range(1):
        tiem = float(input(f"domingo: {i + 1}: "))
        sem.agregar_dia(tiem)

    promedio = sem.prom()

    print(f"El promedio semanal de la temperatura es de: {promedio:.2f} C°")

if __name__ == "__main__":
    ma()






