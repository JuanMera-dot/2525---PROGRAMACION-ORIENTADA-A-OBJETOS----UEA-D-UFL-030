# Agenda personal

# Importación de librerías necesarias
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime

# Ventana principal del calendario
ventana = tk.Tk()
ventana.title("Agenda personal")
ventana.geometry("600x400")  # Tamaño de la ventana principal

# Contenedores (Frames) para organizar la interfaz
frame_eventos = tk.Frame(ventana)
frame_eventos.pack(pady=10)

frame_formulario = tk.Frame(ventana)
frame_formulario.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Tabla para mostrar los eventos
tabla = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripción", text="Descripción")

tabla.column("Fecha", width=100)
tabla.column("Hora", width=80)
tabla.column("Descripción", width=300)
tabla.pack()

# Formulario para ingresar los eventos

# Fecha
tk.Label(frame_formulario, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
ingresar_fecha = DateEntry(frame_formulario, width=12, background="darkblue", foreground="white", date_pattern="yyyy-mm-dd")
ingresar_fecha.grid(row=0, column=1, padx=5, pady=5)

# Hora
tk.Label(frame_formulario, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
ingresar_hora = tk.Entry(frame_formulario)
ingresar_hora.grid(row=0, column=3, padx=5, pady=5)

# Descripción
tk.Label(frame_formulario, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
ingresar_descripcion = tk.Entry(frame_formulario, width=50)
ingresar_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# Función para agregar los elementos a la lista
def agregar_evento():
    fecha = ingresar_fecha.get()
    hora = ingresar_hora.get()
    descripcion = ingresar_descripcion.get()

    # Validación de campos completos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos incompletos", "Por favor complete todos los campos.")
        return

    # Validar formato de hora
    try:
        datetime.datetime.strptime(hora, "%H:%M")
    except ValueError:
        messagebox.showerror("Formato incorrecto", "La hora debe estar en formato HH:MM")
        return

    # Insertar el evento en la tabla
    tabla.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos después de agregar
    ingresar_hora.delete(0, tk.END)
    ingresar_descripcion.delete(0, tk.END)
    ingresar_fecha.set_date(datetime.date.today())  # Reinicia la fecha al día actual

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showinfo("Seleccionar evento", "Por favor selecciona un evento para eliminar.")
        return
    confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")
    if confirmar:
        tabla.delete(seleccionado)

# Cerrar aplicación
def salir():
    ventana.quit()

# Crear los botones de acción y vincular funciones
boton_agregar = tk.Button(frame_botones, text="Agregar evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar evento seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=10)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.grid(row=0, column=2, padx=10)

# Ejecutar la aplicación
ventana.mainloop()


