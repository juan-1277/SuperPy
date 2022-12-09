import tkinter 
from tkinter import *
from tk_Login import login

ventana = tkinter.Tk()
ventana.geometry("800x1000")
ventana.title("Ventana Principal")

#Ventana nueva, para abirir el inicio de sesion. Esta ventana se abre al apretar en el boton INGRESAR
def log_inicio():
    login()

def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
    ventana.destroy()

#Titulo de inicio
etiqueta = tkinter.Label(ventana, text = "BIENVENIDO A SUPERMARK", bg = "blue")
etiqueta.pack(fill = tkinter.X)

#Botones de ingreso al sistema o salida
boton1 = tkinter.Button(ventana, text = "INGRESAR", bg = "orange", command = log_inicio)
boton1.pack()

boton_exit = tkinter.Button(ventana, text = "Exit", bg = "orange", command = close)
boton_exit.pack()




ventana.mainloop()