import tkinter
from tkinter import *
from Database import sql
#from functools import partial
from tkinter import messagebox
from Gui.tk_Carrito import carrito


#Definición de la funcion consulta, que se ejecuta al apretar el boton INGRESAR.
def consulta(email,password):
    print(email)
    print(password)
    global usuario_valido #nuevo
    db = sql.DataBase("superpy.db")
    #usuario_valido = db.select("usuario", "email,password", email, password)
    #usuario_valido = db.select("usuario", "email,password",f'email = {email}')
    #usuario_valido = db.select("usuario", "email,password",f'email = {email}',f'password = {password}')
    usuario_valido = db.select("usuario", "password",f"email = '{email}'")
    
#SOLUCION PROPUESTA
    if len(usuario_valido)>0:
        if password == usuario_valido[0][0]:
            messagebox.showinfo("Inicio", "Inicio de sesión exitoso")
            #ingresar()
            carrito()
            db.close() #siempre cerrar la conexión a la base de datos
            #return usuario_valido #NUEVO
            
        else:
            messagebox.showinfo("Incorrecto", "Contraseña incorrecta")
            #print("Contraseña incorrecta")
    else:
        messagebox.showinfo("User Incorrecto", "No se encuentra Registrado el Usuario")
        #print("Usuario incorrecto ó ")
        #print("No se encuentra Registrado el Usuario")       

#SOLUCION VISTA CON EL PROFE, PENDIENTE DE CORRECCIÒN

    #if (usuario_valido)>0:
     #   if email == usuario_valido[0][0]:
       #     if password == usuario_valido[0][1]:
        #        messagebox.showinfo("Inicio", "Inicio de sesión exitoso")
        #db.close() #siempre cerrar la conexión a la base de datos


#DEFINICION D ELA FUNCION DE APERTURA DEL LOGIN, SE ACTIVA AL EJECUTAR tk_TEST.py
global usuario_entry#NUEVO
def login():
    ventana_inicio = tkinter.Toplevel()
    ventana_inicio.title("Ventana inicio sesion")
    ventana_inicio.geometry("300x200")
    ventana_inicio.configure(bg = "#333333")

    def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
        ventana_inicio.destroy()


    #DEFINICION DE VARIABLES
    global usuario #nuevo
    global usuario_entry#NUEVO
    usuario = StringVar()
    password = StringVar()

    #CREACION DE WIDGETS
    login_label = tkinter.Label(ventana_inicio, text = "LOGIN SUPERMARK")
    usuario_label = tkinter.Label(ventana_inicio, text = "Usuario")
    usuario_entry = tkinter.Entry(ventana_inicio, textvariable=usuario)
    contraseña_label = tkinter.Label(ventana_inicio, text = "Contraseña")
    contraseña_entry = tkinter.Entry(ventana_inicio, textvariable=password)
    boton_login = tkinter.Button(ventana_inicio, text = "INGRESAR", command = lambda : consulta(usuario.get(),password.get()))
    boton_exit = tkinter.Button(ventana_inicio, text = "EXIT", command = close)

    #Colocaciòn de Widgets en pantalla
    login_label.grid(row = 0, column = 0, columnspan = 2)
    usuario_label.grid(row = 1, column = 0)
    usuario_entry.grid(row = 1, column = 1)
    contraseña_label.grid(row = 2, column = 0)
    contraseña_entry.grid(row = 2, column = 1)
    boton_login.grid(row = 3, column = 0, columnspan = 2) 
    boton_exit.grid(row = 5, column = 5)



    ventana_inicio.mainloop()



