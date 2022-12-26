import tkinter
from tkinter import *
from Database import sql
from tkinter import messagebox
from tkinter import ttk

 






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
    tree = ttk.Treeview(ventana_productos, column = ("Categoría","Código","Nombre","Descripción","Precio Venta","Stock"), show='headings')
    # Add a Treeview widget
    tree.column("# 1", anchor=CENTER, width= 60)
    tree.heading("# 1", text="Categoría")
    tree.column("# 2", anchor=CENTER, width= 60)
    tree.heading("# 2", text="Código")
    tree.column("# 3", anchor=CENTER, width= 150)
    tree.heading("# 3", text="Nombre")
    tree.column("# 4", anchor=CENTER, width= 200)
    tree.heading("# 4", text="Descripción")
    tree.column("# 5", anchor=CENTER, width= 60)
    tree.heading("# 5", text="Precio Venta")
    tree.column("# 6", anchor=CENTER, width= 60)
    tree.heading("# 6", text="Stock")
    

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
    productos = db.select_all("producto","id_categoria,codigo,nombre,descripcion,precio_venta,stock")
    for producto in productos:
    # Insert the data in Treeview widget
        tree.insert('','end', text="1",values=((producto[0], producto[1], producto[2], producto[3], producto[4], producto[5])))
    
    tree.place(x = 0, y = 400)
        



####
    db.close()
    
        
    
    ventana_productos.mainloop()

    