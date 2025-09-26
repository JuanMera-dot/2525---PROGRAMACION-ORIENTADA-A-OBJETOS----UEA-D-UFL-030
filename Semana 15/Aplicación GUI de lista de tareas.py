# Importación de librerias necesaria para la interfaz grafica

import tkinter as tk
from tkinter import messagebox

# Ventana principal del programa

ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("400x600")

# Campo de entrada

entrada_de_tarea = tk.Entry(ventana, width=40)
entrada_de_tarea.pack(pady=10)

# Lista de tareas

lista_de_tareas = tk.Listbox(ventana, width=50, selectmode=tk.SINGLE)
lista_de_tareas.pack(pady=10)

# Funcion de añadir tarea

def añadir_tarea():
    tarea = entrada_de_tarea.get()
    if tarea != "":
        lista_de_tareas.insert(tk.END, tarea)
        entrada_de_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Escriba una tarea antes de salir.")

# Funcion de marcar completado

def marcar_complatada():
    seleccion = lista_de_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tarea = lista_de_tareas.get(index)
        if not tarea.startswith("Completada/"):
            tarea = "Completada/" + tarea
            lista_de_tareas.delete(index)
            lista_de_tareas.insert(index, tarea)

# Eliminar tarea

def eliminar_tarea():
    seleccion = lista_de_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        lista_de_tareas.delete(index)

# Botones de ventana

# Boton de añadir
boton_añadir = tk.Button(ventana, text="Añadir tarea", command=añadir_tarea)
boton_añadir.pack(pady=5)

# Boton de completar
boton_completar = tk.Button(ventana, text="Marcar como completada", command=marcar_complatada)
boton_completar.pack(pady=5)

# Boton de eliminar
boton_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Evento Enter para añadir la tarea
entrada_de_tarea.bind("<Return>", lambda event: añadir_tarea())

# Ejecutar la ventana

ventana.mainloop()




