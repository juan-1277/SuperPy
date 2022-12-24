import tkinter 
from tkinter import *
#from Gui.tk_Carrito import carrito
from Gui.tk_Login import login
from Gui.tk_Login_adm import login_adm


def ingresar():
    ventana = tkinter.Toplevel() #eliminar toplevel
    ventana.geometry("800x400")
    ventana.title("Ventana Principal")
    ventana.configure(bg = "dark green")
    #Ventana nueva, para abirir el inicio de sesion. Esta ventana se abre al apretar en el boton INGRESAR
    #def log_inicio():
    #   login()


    def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
        ventana.destroy()

    #Titulo de inicio
    etiqueta = tkinter.Label(ventana, text = "BIENVENIDO A SUPERMARK")
    etiqueta.pack(fill = tkinter.X)

    etiqueta = tkinter.Label(ventana, text = "MAS QUE LA COMIDA, ES LA EXPERIENCIA")
    etiqueta.pack(fill = tkinter.X)

    #Botones de ingreso al sistema o salida
    #boton1 = tkinter.Button(ventana, text = "INGRESAR", bg = "orange", command = carrito)
    boton1 = tkinter.Button(ventana, text = "Ingresar - Cliente", bg = "PaleGreen1", command = login)
    boton1.pack()


    boton2 = tkinter.Button(ventana, text = "Ingresar - Administrador", bg = "PaleGreen1", command = login_adm)
    boton2.pack()

    boton_exit = tkinter.Button(ventana, text = "EXIT", bg = "PaleGreen1", command = close)
    boton_exit.pack()


    ventana.mainloop()