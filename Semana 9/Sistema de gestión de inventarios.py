# Sistema de inventario pra la tienda de celulares CellStore...
# Definimos la clase Dispositivos
class Dispositivos:
    #Inicializamos la clase con sus atributos
    def __init__(self, codigo_producto, marca, cantidad, precio, color):
        self.codigo_producto = codigo_producto
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.color = color


    def __str__(self):
        return f"{self.marca}, Cantidad: {self.cantidad}, Precio: {self.precio}, Color: {self.color}"

# Creamos otra clase que nos permita usar palabras claves para definir las funciones
class Inventario:
    #Inicializamos la clase
    def __init__(self):
        self.dispositivos = {}

    # Agregamos un dispositivo
    def agregar_dispositivo(self, dispositivo):
        if dispositivo.codigo_producto in self.dispositivos:
            print("Ha ocurrido un error: El producto ya existe.")
        else:
            self.dispositivos[dispositivo.codigo_producto] = dispositivo

    # Eliminamos el dispositivo
    def eliminar_dispositivo(self, codigo_producto):
        if codigo_producto in self.dispositivos:
            del self.dispositivos[codigo_producto]
        else:
            print("El dispositivo roducto no ha sido encontrado.")

    # Definimos la funcion para actualizar el dispositivo que el dueño quiera
    def actualizar_dispositivo(self, codigo_producto, cantidad=None, precio=None):
        if codigo_producto in self.dispositivos:
            if cantidad is not None:
                self.dispositivos[codigo_producto].cantidad = cantidad
            if precio is not None:
                self.dispositivos[codigo_producto].precio = precio
            else:
                print("Dispositivo no encontrado.")

    # Definimos la funcion para localizar el dispositivo en el inventario
    def buscar_dispositivo(self, marca):
        for dispositivo in self.dispositivos.values():
            if marca.lower() in dispositivo.marca.lower():
                print(dispositivo)

    # Definimos para mostrar al usuario el inventario
    def mostrar_inventario(self):
        for dispositivo in self.dispositivos.values():
            print(dispositivo)

# Mostramos en consola las opciones que tiene el usuario
def menu():
    inventario = Inventario()

    #Usamos el bucle while para que nos retorne en pantalla las opciones
    while True:
        print("/// Bienvenid@ al sistema de inventario Tienda CellStore ///")
        print("1. Agregar un dispositivo")
        print("2. Eliminar dispositivo")
        print("3. Actualizar dispositivo")
        print("4. Buscar dispositivo")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))

        # Si el usuario elige la opcion 1 se despliegan las opciones para agregar el dispositivo
        if opcion == 1:
            codigo_producto = input("Ingrese el codigo del dispositivo: ")
            marca = str(input("Ingrese la marca del dispositivo: "))
            cantidad = int(input("Ingrese la cantidad de dispositivos: "))
            precio = float(input("Ingrese el precio: "))
            color = str(input("Ingrese el color del dispositivo: "))
            dispositivo = Dispositivos(codigo_producto, marca, cantidad, precio, color)
            inventario.agregar_dispositivo(dispositivo)

        # Si se escoge la opcion dos permite eliminar el dispositivo siempre y cuando tenga el codigo
        elif opcion == 2:
            codigo_producto = input("Ingrese el codigo de dispositivo a eliminar: ")
            inventario.eliminar_dispositivo(codigo_producto)

        # Con la opcion tres definimos nuevas opciones que permitan cambiar o actualizar el producto
        elif opcion == 3:
            codigo_producto = input("Ingrese el codigo de dispositivo a actulizar: ")
            cantidad = int(input("Ingrese la nueva cantidad de dispositivos: "))
            precio = float(input("Ingrese el nuevo precio: "))
            color = str(input("Ingrese el nuevo color: "))
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            color = str(color) if color else None
            inventario.actualizar_dispositivo(codigo_producto, cantidad, precio, color)

        # Opcion cuatro buscamos el dispositivo
        elif opcion == 4:
            marca = input("Ingrese la marca del dispositivo a buscar: ")
            inventario.buscar_dispositivo(marca)

        # Opcion cinco mostramos el inventario
        elif opcion == 5:
            inventario.mostrar_inventario()

        # Si se elije la opcion seis se detiene el programa
        elif opcion == 6:
            break

if __name__ == "__main__":
    menu()






