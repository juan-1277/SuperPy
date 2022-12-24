import tkinter
from tkinter import *
from Proyecto.producto import Producto


def creacion_producto():
    producto = Producto()
    producto.crearProducto()   




def menu():
    ventana = tkinter.Toplevel() #eliminar toplevel
    ventana.geometry("400x300")
    ventana.title("MENU")
    #label = tkinter.Label(ventana, text = "LOGIN SUPERMARK")
    ventana.configure(bg = "blue4")

    def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
        ventana.destroy()

    

    boton1 = tkinter.Button(ventana, text = "Productos", bg = "orange", command = creacion_producto)
    boton1.pack()

    boton2 = tkinter.Button(ventana, text = "Usuarios", bg = "orange")
    boton2.pack()

    boton3 = tkinter.Button(ventana, text = "Ventas", bg = "orange")
    boton3.pack()

    boton_exit = tkinter.Button(ventana, text = "Exit", bg = "orange", command = close)
    boton_exit.pack()

    ventana.mainloop()