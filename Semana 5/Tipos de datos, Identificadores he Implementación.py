# Calculadora sencilla con operaciones basicas

# Imprimimos en pantalla las opciones de operaciones que tiene el usuario
print("/// Calculadora ///")
print()
print("OPERACIONES")
print("Opción_uno: Suma")
print("Opción_dos: Resta")
print("Opción_tres: Multiplicación")
print("Opción_cuatro: División")

# Pedimos al usuario que ingrese la opcion que desea calular en numeros
print()
opcion = int(input("Ingresa la opción que deseas: "))

# Realizamos las operaciones conforme a la opcion que solicitó el usuario
print()
if opcion == 1:
    print("Elegiste suma")
    print()
    numero_uno = float(input("Ingresa el primer valor: "))
    numero_dos = float(input("Ingresa el segundo valor: "))
    resultado = numero_uno + numero_dos
    print()
    print(f"El resultado es: {resultado}")

elif opcion == 2:
    print("Elegiste resta")
    print()
    numero_uno = float(input("Ingresa el primer valor: "))
    numero_dos = float(input("Ingresa el segundo valor: "))
    resultado = numero_uno - numero_dos
    print()
    print(f"El resultado es: {resultado}")

elif opcion == 3:
    print("Elegiste multiplicación")
    print()
    numero_uno = float(input("Ingresa el primer valor: "))
    numero_dos = float(input("Ingresa el segundo valor: "))
    resultado = numero_uno * numero_dos
    print()
    print(f"El resultado es: {resultado}")

elif opcion == 4:
    print("Elegiste división")
    print()
    numero_uno = float(input("Ingresa el primer valor: "))
    numero_dos = float(input("Ingresa el segundo valor: "))
    resultado = numero_uno / numero_dos
    print()
    print(f"El resultado es: {resultado}")

# Escribimos el else con el fin de que el programa identifique que una de las opciones que puso el usuario
# no está en pantalla y mostrandole en panatalla de que no se encuentra
else:
    print("El valor ingresado no está en una de las opciones")



