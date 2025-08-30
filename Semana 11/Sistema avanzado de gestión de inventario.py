# Sistema de inventario pra la tienda de celulares CellStore..

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
        return f"{self.codigo_producto} - {self.marca}, Cantidad: {self.cantidad}, Precio: {self.precio}, Color: {self.color}"

    def linea(self):
        return f"{self.codigo_producto}, {self.marca}, {self.cantidad}, {self.precio}, {self.color}"

    #Usamos @staticmethod para declarar un metodo dentro de una clase
    @staticmethod
    def from_line(lineas):
        try:
            codigo, marca, cantidad, precio, color = lineas.strip().split(",")
            return Dispositivos(codigo, marca, int(cantidad), float(precio), color)
        except ValueError:
            return None


# Creamos otra clase que nos permita usar palabras claves para definir las funciones
class Inventario:
    #Inicializamos la clase
    def __init__(self):
        self.dispositivos = {}
        self.archivo = "Inventario.txt"
        self.cargar_desde_archivo()

    #Se guarda el archivo y se usa las excepciones para evitar errores en consola
    def guargar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for dispositivo in self.dispositivos.values():
                    f.write(dispositivo.linea() + "\n")
            print("El inventario ha sido guardado correctamente.")
        except PermissionError:
            print("Error: Solicita primero permiso para escribir al propietario.")
        except Exception as e:
            print(f"Hubo un error al guardar en el archivo: {e}")

    #Cargamos los datos desde el archivo usando excepciones y r para leer el archivo
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea_redaccion in f:
                    dispositivo = Dispositivos.from_line(linea_redaccion)
                    if dispositivo:
                        self.dispositivos[dispositivo.codigo_producto] = dispositivo
            print("Inventario ha iniciado correctamente.")
        except FileExistsError:
            print("No se ha encontrado el archivo: Se procederá a crear uno nuevo al gaurdar los cambios.")
        except PermissionError:
            print("Error: No tiene permiso para acceder al archivo.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e} ")

    # Agregamos un dispositivo
    def agregar_dispositivo(self, dispositivo):
        if dispositivo.codigo_producto in self.dispositivos:
            print("Ha ocurrido un error: El producto ya existe.")
        else:
            self.dispositivos[dispositivo.codigo_producto] = dispositivo
            self.guargar_en_archivo()
            print("Dispositivo agregado correctamente.")

    # Eliminamos el dispositivo
    def eliminar_dispositivo(self, codigo_producto):
        if codigo_producto in self.dispositivos:
            del self.dispositivos[codigo_producto]
            self.guargar_en_archivo()
            print("El dispositivo ha sido eliminado correctamente.")
        else:
            print("El dispositivo producto no ha sido encontrado.")

    # Definimos la funcion para actualizar el dispositivo que el dueño quiera
    def actualizar_dispositivo(self, codigo_producto, cantidad=None, precio=None, color=None):
        if codigo_producto in self.dispositivos:
            dispositivo = self.dispositivos[codigo_producto]
            if cantidad is not None:
                dispositivo.cantidad = cantidad
            if precio is not None:
                dispositivo.precio = precio
            if color is not None:
                dispositivo.color = color
            self.guargar_en_archivo()
            print("Dispositivo actualizado exitosamente.")
        else:
            print("Dispositivo no encontrado.")

    # Definimos la funcion para localizar el dispositivo en el inventario
    def buscar_dispositivo(self, marca):
        encontrados = False
        for dispositivo in self.dispositivos.values():
            if marca.lower() in dispositivo.marca.lower():
                print(dispositivo)
                encontrados = True
        if not encontrados:
            print("No se han encontrado dispositivos con esa marca.")

    # Definimos para mostrar al usuario el inventario
    def mostrar_inventario(self):
        if not self.dispositivos:
            print("El inventario está vacío.")
        else:
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
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor ingrese un número valido.")
            continue

        # Si el usuario elige la opcion 1 se despliegan las opciones para agregar el dispositivo
        if opcion == 1:
            codigo_producto = input("Ingrese el codigo del dispositivo: ")
            marca = str(input("Ingrese la marca del dispositivo: "))
            try:
                cantidad = int(input("Ingrese la cantidad de dispositivos: "))
                precio = float(input("Ingrese el precio: "))
            except ValueError:
                print("Error: Cantidad y precio deben ser datos numericos.")
                continue
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
            try:
                cantidad = int(input("Ingrese la nueva cantidad de dispositivos: "))
                precio = float(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Error: Cantidad y precio deben ser datos numericos.")
                continue
            color = str(input("Ingrese el nuevo color: "))
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
            print("Saliendo del sistema..¡HASTA PRONTO!")
            break

        else:
            print("Opción no valida..intente nuevamente.")

if __name__ == "__main__":
    menu()
