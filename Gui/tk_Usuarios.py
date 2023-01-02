import tkinter
from tkinter import *
from Database import sql
from tkinter import ttk

def usuarios():
    ventana_usuarios= tkinter.Tk() 
    ventana_usuarios.geometry("800x400")
    ventana_usuarios.title("Lista de usuarios")
    ventana_usuarios.configure(bg = "blue4")    

    tree_usuarios = ttk.Treeview(ventana_usuarios, column = ("id_usuario","nombre","apellido","dni","email", "password"), show='headings',height=4)
    tree_usuarios.column("# 1", anchor=CENTER, width= 60)
    tree_usuarios.heading("# 1", text="ID usuario")
    tree_usuarios.column("# 2", anchor=CENTER, width= 60)
    tree_usuarios.heading("# 2", text="Nombre")
    tree_usuarios.column("# 3", anchor=CENTER, width= 60)
    tree_usuarios.heading("# 3", text="Apellido")
    tree_usuarios.column("# 4", anchor=CENTER, width= 60)
    tree_usuarios.heading("# 4", text="DNI")
    tree_usuarios.column("# 5", anchor=CENTER, width= 200)
    tree_usuarios.heading("# 5", text="Email")
    tree_usuarios.column("# 6", anchor=CENTER, width= 100)
    tree_usuarios.heading("# 6", text="Password")

    usuarios_label=tkinter.Label(ventana_usuarios,text="LISTA DE USUARIOS")
    usuarios_label.grid(row=0,column=1)
    
    tree_usuarios.grid(row=3,column=1)

    db = sql.DataBase("superpy.db")
    usuarios = db.select_all("usuario","id_usuario,nombre,apellido,dni,email,password")

    for usuario in usuarios:
        tree_usuarios.insert('','end', text="1",values=((usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5])))     