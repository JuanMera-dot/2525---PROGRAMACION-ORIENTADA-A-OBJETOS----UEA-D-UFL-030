# Determinar el promedio semanal de temperaturas
# Creamos una lista con las temperaturas por cada día

print("Calculo de temperatura semanal")

print()

# Solicitamos al usuario que coloque por cada dia de la semana la temperatura que alcanzo esos dias
# Usamos el tipo de dato FLOAT para que el usuario pueda ingresar numeros con decimales

dia_uno = float(input("Ingrese la temperatura del día lunes: "))
dia_dos = float(input("Ingrese la temperatura del día martes: "))
dia_tres = float(input("Ingrese la temperatura del día miercoles: "))
dia_cuatro = float(input("Ingrese la temperatura del día jueves: "))
dia_cinco = float(input("Ingrese la temperatura del día viernes: "))
dia_seis = float(input("Ingrese la temperatura del día sabado: "))
dia_siete = float(input("Ingrese la temperatura del día domingo: "))

# Calcularmos el promedio sumando las temperaturas de los dias y dividiendolas para la cantidad de datos insertada

prom = ((dia_uno + dia_dos + dia_tres + dia_cuatro + dia_cinco + dia_seis + dia_siete) / 7)

# Usamos la funcion ROUND para que al momento de obtener el promedio solo nos de un alcance de dos decimales

red = round(prom, 2)

print()

print("El promedio de la temperatura semanal es de:  ", red, "g°")
