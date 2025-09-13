#Importamos la librería tkinter para empezar con la interfaz gráfica

import tkinter as tk
from tkinter import messagebox, Listbox

# Agregamos la funcion de agregar los datos en la lista que el usuario quiera
def agregar_datos():
    datos = entrada_de_datos.get()
    if datos.strip():
        lista.insert(tk.END, datos)
        entrada_de_datos.delete(0,tk.END)
    else:
        messagebox.showinfo("El campo está vacío", "Por favor ingresa algún dato." )

# Se agrega la función de eliminar los datos en caso de que el usuario lo quiera así

def limpiar_lista():
    lista.delete(0, tk.END)

# Modificamos el aspecto que va a tener la ventana como su tamaño, el titulo y el color

ventana = tk.Tk()
ventana.title("Administrador de datos - GUI")
ventana.geometry("400x400")
ventana.configure(bg="#1e1e1e")

frame = tk.Frame(ventana, bg= "#1e1e1e")
frame.pack(pady=20)

# Agregamos las etiquetas y los atributos con la cual se va a ingresar los datos

etiqueta = tk.Label(frame, text="Ingresa un dato", fg="white", bg="#1e1e1e", font=("Arial", 12))
etiqueta.grid(row=0, column=0, padx=5, pady=5)

entrada_de_datos = tk.Entry(frame, width=30)
entrada_de_datos.grid(row=0, column=1, padx=5, pady=5)

# Modificamos el boton de agregar datos como el titulo, color y la fuente

agregar_boton = tk.Button(
    frame,
    text = "Agregar",
    command = agregar_datos,
    bg = "#27ae60",
    fg = "white",
    font = ("Arial", 10, "bold")
)
agregar_boton.grid(row=1, column=0, columnspan=2, pady=10, ipadx=20)

lista = tk.Listbox(ventana, width=45, height=10)
lista.pack(pady=10)

# Modificamos el boton con el cual el ususario va a eliminar la lista

boton_limpiar = tk.Button(
    ventana,
    text = "Limpiar lista",
    command = limpiar_lista,
    bg = "#c0392b",
    font = ("Arial", 10, "bold"),
    fg = "white"
)
boton_limpiar.pack(pady=10, ipadx=10)

# Inicializamos el programa

ventana.mainloop()