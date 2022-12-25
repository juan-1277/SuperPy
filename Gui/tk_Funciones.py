import tkinter
from tkinter import *
from Database import sql


 






def informacion_productos():
    ventana_productos = tkinter.Tk() 
    ventana_productos.geometry("500x500")
    ventana_productos.title("Informacion relevante para el producto")
    ventana_productos.configure(bg = "blue4")


    #CREACION DE WIDGETS
    id_producto_label = tkinter.Label(ventana_productos, text = "Ingrese ID del producto")
    codigo_label = tkinter.Label(ventana_productos, text = "Ingrese el codigo del producto: ")
    nombre_label = tkinter.Label(ventana_productos, text = "Ingrese el nombre del producto: ")
    precio_label = tkinter.Label(ventana_productos, text = "Ingrese el precio del prdocuto: ")
    stock_label = tkinter.Label(ventana_productos, text = "Ingrese el stock del producto: ")
    descripcion_label = tkinter.Label(ventana_productos, text = "Ingrese la descripciòn: ")
    categoria_label = tkinter.Label(ventana_productos, text ="Ingrese la categorìa del producto")

    def crear_producto():
        db = sql.DataBase("superpy.db")
        db.insert("producto","id_producto,id_categoria,codigo,nombre,precio_venta", f"{id_producto_entry},'{categoria_entry}','{codigo_entry}',{nombre_entry}','{precio_entry}'")
        db.close()

    cargar_producto = tkinter.Button(ventana_productos, text = "CREAR", command = crear_producto)

    id_producto_entry = tkinter.Entry(ventana_productos)
    codigo_entry = tkinter.Entry(ventana_productos)
    nombre_entry = tkinter.Entry(ventana_productos)
    precio_entry = tkinter.Entry(ventana_productos)
    stock_entry = tkinter.Entry(ventana_productos)
    descripcion = tkinter.Entry(ventana_productos)
    categoria_entry = tkinter.Entry(ventana_productos)
    categorìas_label = tkinter.Label(ventana_productos, text = "Categorìas")
    descripcion_categorias_label = tkinter.Label(ventana_productos, text = "Descripciones")
    id_categorias_label = tkinter.Label(ventana_productos, text = "ID Categorìa")
    categorìas_listbox = tkinter.Listbox(ventana_productos)# LISTA DE PRODUCTOS EN CATALOGO    
    descripcion_categorias_listbox = tkinter.Listbox(ventana_productos)#LISTA DE PRECIOS EN CATALOGO
    idcategorias_listbox = tkinter.Listbox(ventana_productos)
    #COLOCACION DE WIDGETS EN PANTALLA
    id_producto_label.grid(row = 1, column = 1)
    codigo_label.grid(row = 2, column = 1)
    nombre_label.grid(row = 3, column = 1)
    precio_label.grid(row = 4, column = 1)
    stock_label.grid(row = 5, column = 1)
    descripcion_label.grid(row = 6, column = 1) 

    id_producto_entry.grid(row = 1, column = 2)
    codigo_entry.grid(row = 2, column = 2) 
    nombre_entry.grid(row = 3, column = 2)
    precio_entry.grid(row = 4, column = 2) 
    stock_entry.grid(row = 5, column = 2) 
    descripcion.grid(row = 6, column = 2) 
    categoria_label.grid(row = 7, column = 1) 
    categoria_entry.grid(row = 7, column = 2)

    id_categorias_label.grid(row = 8, column = 1)
    categorìas_label.grid(row = 8, column = 2)
    descripcion_categorias_label.grid(row = 8, column = 3)
    
    idcategorias_listbox.grid(row = 9, column = 1)
    categorìas_listbox.grid(row = 9, column = 2)    
    descripcion_categorias_listbox.grid(row = 9, column = 3)
    cargar_producto.grid(row = 10, column = 7)
    

    db = sql.DataBase('superpy.db')
    categorias = db.select_all("categoria","id_categoria,nombre,descripcion")
    #print("Nro\tNombre")
    #for categoria in categorias:
      #  print(f"{categoria[0]}\t{categoria[1]}")

    for categoria in categorias:
        idcategorias_listbox.insert(END, categoria[0])

    for categoria in categorias:
        categorìas_listbox.insert(END, categoria[1])

    for categoria in categorias:
        descripcion_categorias_listbox.insert(END, categoria[2])
####

    
    
    
    ventana_productos.mainloop()

    