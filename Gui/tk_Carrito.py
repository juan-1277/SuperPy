import tkinter
from tkinter import *

def carrito ():
    #DEFINICION DE LA VENTANA Y CARACTERISTICAS
    ventana_carrito = tkinter.Tk()
    ventana_carrito.geometry("800x400")
    ventana_carrito.title("Carro de compras")
    ventana_carrito.configure(bg = "green")
    producto = StringVar()

    ########DEFINICION DE FUNCIONES##########

    #LE FALTA CODEARLE QUE NO PERMITA AGREGAR SI ES QUE EL PRODUCTO NO ESTA EN LA BASE DE DATOS
    #ESTA FUNCION PERMITE AGREGAR PRODUCTOS EN LA LISTA DE PRODUCTOS
    def agregar_productosycantidades(): 
        lista_productos.insert(END, producto.get())
        lista_cantidades.insert(END, cantidad_entry.get())

    #def agregar_cantidad():#ESTA FUNCION PERMITE AGREGAR PRODUCTOS EN LA LISTA DE CANTIDADES
        #lista_cantidades.insert(END, cantidad_entry.get())

    def eliminar_productosycantidades():#ESTA FUNCION PERMITE ELIMINAR PRODUCTOS Y CANTIDADES AL MISMO TIEMPO
        indice = int(eliminar_entry.get())
        lista_productos.delete(indice - 1)
        lista_cantidades.delete(indice - 1)

    #FALTA DEFINIR BIEN LA FUNCION DE BUSCAR, VER CON EL PROFE COMO CREAR LA BASE DE DATOS DEL PRODUCTO.
    #LA FUNCION DEBERIA PERMITIR VER SI EL PRODUCTO QUE SE ESTA CARGANDO ESTA DISPONIBLE, Y EN CASO DE QUE ESTÉ, QUE DE EL AVISO.
    #def buscar(producto): 
            #db = sql.DataBase("superpy.db")
            #producto_valido = db.select("usuario", "email,password",f'email = {email}',f'password = {password}')

        # if email == usuario_valido[0][0]:
            #    if password == usuario_valido[0][1]:
            #       tkinter.messagebox.showinfo(title="Inicio", message="Inicio de sesión exitoso")
            #db.close() #siempre cerrar la conexión a la base de datos






    ###########Creaciòn de Widgets


    titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
    total_label = tkinter.Label(ventana_carrito, text = "Total a pagar $")
    lista_label = tkinter.Label(ventana_carrito, text = "Lista de productos")
    cantidades_label = tkinter.Label(ventana_carrito, text = "Cantidades")
    agregar_producto_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = agregar_productosycantidades, bg = "SkyBlue1")
    #agregar_cantidad_boton = tkinter.Button(ventana_carrito, text = "AGREGAR Q", command = agregar_cantidad)
    buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR", bg = "gray64")
    ingresar_label = tkinter.Label(ventana_carrito , text = "Ingresar un producto")
    cantidad_label = tkinter.Label(ventana_carrito , text = "Ingresar cantidad")
    cantidad_entry = tkinter.Spinbox(ventana_carrito)
    txt_producto = tkinter.Entry(ventana_carrito, textvariable = producto)
    lista_productos = tkinter.Listbox(ventana_carrito)
    lista_cantidades = tkinter.Listbox(ventana_carrito)
    eliminar_label = tkinter.Label(ventana_carrito, text = "Posición a eliminar")
    eliminar_entry = tkinter.Spinbox(ventana_carrito)   
    eliminar_boton = tkinter.Button(ventana_carrito, text = "ELIMINAR", command = eliminar_productosycantidades, bg = "red")


    ###########   Colocaciòn de Widgets en pantalla


    titulo_label.grid(row = 0, column = 3)
    total_label.grid(row = 1, column = 6)
    lista_label.grid(row = 2, column = 1)
    cantidades_label.grid(row = 2, column = 2)
    agregar_producto_boton.grid(row = 4, column = 7)
    #agregar_cantidad_boton.grid(row = 5, column = 6)
    buscar_boton.grid(row = 4, column = 6)
    ingresar_label.grid(row = 4, column = 3)
    cantidad_label.grid(row = 5, column = 3)
    cantidad_entry.grid(row = 5, column = 5)
    txt_producto.grid(row = 4, column = 5)
    lista_productos.grid(row = 5, column = 1)
    lista_cantidades.grid(row = 5, column = 2)
    eliminar_label.grid(row = 7, column = 1)
    eliminar_entry.grid(row = 7, column = 2)
    eliminar_boton.grid(row = 7, column = 3)




    ventana_carrito.mainloop()