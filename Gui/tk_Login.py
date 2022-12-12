import tkinter
from tkinter import *
from Database import sql
from functools import partial
from tkinter import messagebox

def consulta(email,password):
    db = sql.DataBase("superpy.db")
    #usuario_valido = db.select("usuario", "email,password", email, password)
    #usuario_valido = db.select("usuario", "email,password",f'email = {email}')
    #usuario_valido = db.select("usuario", "email,password",f'email = {email}',f'password = {password}')
    usuario_valido = db.select("usuario", "password",f"email = '{email}'")

#SOLUCION PROPUESTA
    if (usuario_valido)>0:
        password = usuario_valido[0][0]
        if password == password:
            messagebox.showinfo("Inicio", "Inicio de sesión exitoso")
            db.close() #siempre cerrar la conexión a la base de datos
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario incorrecto ó ")
        print("No se encuentra Registrado el Usuario")       

#SOLUCION VISTA CON EL PROFE, PENDIENTE DE CORRECCIÒN

    #if (usuario_valido)>0:
     #   if email == usuario_valido[0][0]:
       #     if password == usuario_valido[0][1]:
        #        messagebox.showinfo("Inicio", "Inicio de sesión exitoso")
        #db.close() #siempre cerrar la conexión a la base de datos

def login():
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
    boton_login = tkinter.Button(ventana_inicio, text = "INGRESAR", command = partial(consulta,(usuario_entry.get()), (contraseña_entry.get())))
 
    #Colocaciòn de Widgets en pantalla

    login_label.grid(row = 0, column = 0, columnspan = 2)
    usuario_label.grid(row = 1, column = 0)
    usuario_entry.grid(row = 1, column = 1)
    contraseña_label.grid(row = 2, column = 0)
    contraseña_entry.grid(row = 2, column = 1)
    boton_login.grid(row = 3, column = 0, columnspan = 2) 

    

    

    ventana_inicio.mainloop()



