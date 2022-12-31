import tkinter
from tkinter import *
from Gui.tk_Funciones import informacion_productos


#def creacion_producto():
 #   producto = Producto()
  #  producto.crearProducto()   




def menu():
    ventana = tkinter.Tk() #eliminar toplevel
    ventana.geometry("400x400")
    ventana.title("MENU")
    #label = tkinter.Label(ventana, text = "LOGIN SUPERMARK")
    ventana.configure(bg = "blue4")

    def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
        ventana.destroy()

    
    presentacion_adm = tkinter.Label(ventana, text = "Bienvendio al modo administrador")
    presentacion_adm.place(x=0, y = 0)

    boton1 = tkinter.Button(ventana, text = "Productos", bg = "medium orchid", command = informacion_productos)
    boton1.place(x=200, y = 100)

    boton2 = tkinter.Button(ventana, text = "Usuarios", bg = "medium orchid")
    boton2.place(x=204, y = 125)

    boton3 = tkinter.Button(ventana, text = "Ventas", bg = "medium orchid")
    boton3.place(x=205, y = 150)

    boton_exit = tkinter.Button(ventana, text = "Exit", bg = "medium orchid", command = close)
    boton_exit.place(x=200, y = 175)
    ventana.mainloop()