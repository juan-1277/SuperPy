import tkinter
from tkinter import *

ventana_inicio = tkinter.Tk()
ventana_inicio.title("Ventana inicio sesion")
ventana_inicio.geometry("300x200")
ventana_inicio.configure(bg = "#333333")

#Creaciòn de Widgets

login_label = tkinter.Label(ventana_inicio, text = "LOGIN SUPERMARK")
usuario_label = tkinter.Label(ventana_inicio, text = "Usuario")
usuario_entry = tkinter.Entry(ventana_inicio)
contraseña_label = tkinter.Label(ventana_inicio, text = "Contraseña")
contraseña_entry = tkinter.Entry(ventana_inicio)
boton_login = tkinter.Button(ventana_inicio, text = "INGRESAR")

#Colocaciòn de Widgets en pantalla

login_label.grid(row = 0, column = 0, columnspan = 2)
usuario_label.grid(row = 1, column = 0)
usuario_entry.grid(row = 1, column = 1)
contraseña_label.grid(row = 2, column = 0)
contraseña_entry.grid(row = 2, column = 1)
boton_login.grid(row = 3, column = 0, columnspan = 2) 


ventana_inicio.mainloop()