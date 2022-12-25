import tkinter
from tkinter import *
from Database import sql
from tkinter import messagebox

 






def informacion_productos():
    ventana_productos = tkinter.Tk() 
    ventana_productos.geometry("1200x800")
    ventana_productos.title("Informacion relevante para el producto")
    ventana_productos.configure(bg = "blue4")

    def crear_producto():
        if len(categoria_entry.get()) > 0 and len(codigo_entry.get()) > 0 and len(nombre_entry.get()) > 0 and len(precio_entry.get()) > 0 and len(stock_entry.get()) > 0 and len(descripcion_entry.get()) > 0:
            db = sql.DataBase("superpy.db")
            db.insert('producto','id_categoria,codigo,nombre,precio_venta,stock,descripcion', f'"{categoria_entry.get()}","{codigo_entry.get()}","{nombre_entry.get()}","{precio_entry.get()}","{stock_entry.get()}","{descripcion_entry.get()}"')
            messagebox.showinfo("Agregado", "El producto se ha agregado.")
            db.close()  
        else:
            messagebox.showerror("ERROR", "El producto NO se ha agregado, revise los datos ingresados.")
        
    #CREACION DE WIDGETS
    id_producto_label = tkinter.Label(ventana_productos, text = "Ingrese ID del producto")
    codigo_label = tkinter.Label(ventana_productos, text = "Ingrese el codigo del producto: ")
    nombre_label = tkinter.Label(ventana_productos, text = "Ingrese el nombre del producto: ")
    precio_label = tkinter.Label(ventana_productos, text = "Ingrese el precio del prdocuto: ")
    stock_label = tkinter.Label(ventana_productos, text = "Ingrese el stock del producto: ")
    descripcion_label = tkinter.Label(ventana_productos, text = "Ingrese la descripciòn: ")
    categoria_label = tkinter.Label(ventana_productos, text ="Ingrese la categorìa del producto")

    lista_categorias_label = tkinter.Label(ventana_productos, text = "Categorìa")
    lista_codigos_label = tkinter.Label(ventana_productos, text = "Codigo")
    lista_nombre_label = tkinter.Label(ventana_productos, text = "Nombre")
    lista_descripcion_label = tkinter.Label(ventana_productos, text = "Descripcion")
    lista_precio_label = tkinter.Label(ventana_productos, text = "Precio")
    lista_stock_label = tkinter.Label(ventana_productos, text = "Stock")
    





    id_producto_entry = tkinter.Entry(ventana_productos)
    codigo_entry = tkinter.Entry(ventana_productos)
    nombre_entry = tkinter.Entry(ventana_productos)
    precio_entry = tkinter.Entry(ventana_productos)
    stock_entry = tkinter.Entry(ventana_productos)
    descripcion_entry = tkinter.Entry(ventana_productos)
    categoria_entry = tkinter.Entry(ventana_productos)
    categorìas_label = tkinter.Label(ventana_productos, text = "Categorìas")
    descripcion_categorias_label = tkinter.Label(ventana_productos, text = "Descripciones")
    id_categorias_label = tkinter.Label(ventana_productos, text = "ID Categorìa")
    categorìas_listbox = tkinter.Listbox(ventana_productos)# LISTA DE PRODUCTOS EN CATALOGO    
    descripcion_categorias_listbox = tkinter.Listbox(ventana_productos, width=50)#LISTA DE PRECIOS EN CATALOGO
    idcategorias_listbox = tkinter.Listbox(ventana_productos)

    lista_categorias = tkinter.Listbox(ventana_productos)
    lista_codigo = tkinter.Listbox(ventana_productos)
    lista_nombre = tkinter.Listbox(ventana_productos)
    lista_precio = tkinter.Listbox(ventana_productos)
    lista_stock = tkinter.Listbox(ventana_productos)
    lista_descripcion = tkinter.Listbox(ventana_productos)

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
    descripcion_entry.grid(row = 6, column = 2) 
    categoria_label.grid(row = 7, column = 1) 
    categoria_entry.grid(row = 7, column = 2)

    id_categorias_label.grid(row = 8, column = 1)
    categorìas_label.grid(row = 8, column = 2)
    descripcion_categorias_label.grid(row = 8, column = 3)
    
    idcategorias_listbox.grid(row = 9, column = 1)
    categorìas_listbox.grid(row = 9, column = 2)    
    descripcion_categorias_listbox.grid(row = 9, column = 3)

    

    cargar_producto = tkinter.Button(ventana_productos, text = "CREAR", command = crear_producto)
    cargar_producto.grid(row = 10, column = 7)
    

    lista_categorias_label.grid(row = 11, column = 1)
    lista_codigos_label.grid(row = 11, column = 2)
    lista_nombre_label.grid(row = 11, column = 3)
    lista_descripcion_label.grid(row = 11, column = 4)
    lista_precio_label.grid(row = 11, column = 5)
    lista_stock_label.grid(row = 11, column = 6) 


    lista_categorias.grid(row = 12, column = 1)
    lista_codigo.grid(row = 12, column = 2)
    lista_nombre.grid(row = 12, column = 3)
    lista_precio.grid(row = 12, column = 4)
    lista_stock.grid(row = 12, column = 5)
    lista_descripcion.grid(row = 12, column = 6)






    #LISTAS PARA MOSTRAR LAS CATEGORIAS DISPONIBLES

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

    #LISTAS PARA MOSTRAR LOS PRODUCTOS EN LA BASE DE DATOS
    db = sql.DataBase('superpy.db')
    productos = db.select_all("producto","id_categoria,codigo,nombre,precio_venta,stock,descripcion")
    

    for producto in productos:
        lista_categorias.insert(END, producto[0])

    for producto in productos:
        lista_codigo.insert(END, producto[1])

    for producto in productos:
        lista_nombre.insert(END, producto[2])

    for producto in productos:
        lista_precio.insert(END, producto[3])    
    
    for producto in productos:
        lista_stock.insert(END, producto[4])

    for producto in productos:
        lista_descripcion.insert(END, producto[5])  














####
    db.close()
    
        
    
    ventana_productos.mainloop()

    