# Importacion de librerias necesarias

import tkinter as tk
from tkinter import messagebox

# Ventana principal de la aplicación

ventana = tk.Tk()
ventana.title("Gestión de tareas")
ventana.geometry("400x400")

# Entrada de tareas

entrada_tareas = tk.Entry(ventana, width=40)
entrada_tareas.pack(pady=10)

# lista de tareas

lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

# Funciones

# Agregar tarea
def agregar_tarea(event=None):
    tarea = entrada_tareas.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tareas.delete(0, tk.END)

# Marcar completadda la tarea
def marcar_completado(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tarea = lista_tareas.get(index)
        if not tarea.startswith("Tarea completada/"):
            lista_tareas.delete(index)
            lista_tareas.insert(index, "Tarea completada/" + tarea)
            lista_tareas.itemconfig(index, {'fg': 'gray'})

# Eliminar tarea
def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])

# Cerrar aplicacion
def cerrar_aplicacion(event=None):
    ventana.destroy()

# Botones

tk.Button(ventana, text="Añadir tareas", command=agregar_tarea).pack()
tk.Button(ventana, text="Marcar como completada", command=marcar_completado).pack()
tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea).pack()

# Atajos en el teclado
ventana.bind('<Return>', agregar_tarea)
ventana.bind('<c>', marcar_completado)
ventana.bind('<C>', marcar_completado)
ventana.bind('<Delete>', eliminar_tarea)
ventana.bind('<d>', eliminar_tarea)
ventana.bind('<Escape>', cerrar_aplicacion)

ventana.bind('<D>', eliminar_tarea)

# Ejecutar aplicación
ventana.mainloop()

