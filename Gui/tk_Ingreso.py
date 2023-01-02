import tkinter 
from tkinter import *
#from Gui.tk_Carrito import carrito
from Gui.tk_Login import login
from Gui.tk_Login_adm import login_adm

def ingresar():
    ventana = tkinter.Tk() #eliminar toplevel
    ventana.geometry("800x400")
    ventana.title("Ventana Principal")
    ventana.configure(bg = "blue4")
    
    def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
        ventana.destroy()
    #Titulo de inicio
    etiqueta = tkinter.Label(ventana, text = "BIENVENIDO A SUPERMARK")
    etiqueta.pack(fill = tkinter.X)

    etiqueta = tkinter.Label(ventana, text = "MAS QUE LA COMIDA, ES LA EXPERIENCIA")
    etiqueta.pack(fill = tkinter.X)

    #Botones de ingreso al sistema o salida
    #boton1 = tkinter.Button(ventana, text = "INGRESAR", bg = "orange", command = carrito)
    boton1 = tkinter.Button(ventana, text = "Ingresar - Cliente", bg = "medium orchid", command = login)
    boton1.place(x=350,y=100)


    boton2 = tkinter.Button(ventana, text = "Ingresar - Administrador", bg = "medium orchid", command = login_adm)
    boton2.place(x=331,y=150)

    boton_exit = tkinter.Button(ventana, text = "EXIT", bg = "medium orchid", command = close)
    boton_exit.place(x=385,y=200)


    ventana.mainloop()