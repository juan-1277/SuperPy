import tkinter
from tkinter import *
from Database import sql
from tkinter import ttk
#from Gui.tk_Carrito import carrito

def catalogo():
    ventana_catalogo = tkinter.Toplevel()
    ventana_catalogo.geometry("800x400")
    ventana_catalogo.title("Catalogo de Productos")
    ventana_catalogo.configure(bg = "blue4")
#
 #   db = sql.DataBase("superpy.db")
  #  
   # producto_valido = db.select_all("producto","nombre,precio_venta")
#    catalogo_lista_producto = tkinter.Listbox(ventana_catalogo)
 #   catalogo_lista_precio = tkinter.Listbox(ventana_catalogo)
#
 #   for producto in producto_valido:
  #      catalogo_lista_producto.insert(END, producto[0])

   # for producto in producto_valido:
    #    catalogo_lista_precio.insert(END, producto[1])

    #WIDGETS EN PANTALLA
#    catalogo_lista_producto.grid(row = 2, column = 2)
 #   catalogo_lista_precio.grid(row = 2, column = 3)

     #LISTAS PARA MOSTRAR LOS PRODUCTOS EN LA BASE DE DATOS
    tree = ttk.Treeview(ventana_catalogo, column = ("Categoría","Código","Nombre","Descripción","Precio Venta","Stock"), show='headings')
    # Add a Treeview widget CORRESPONDE AL TREEVIEW DE LOS PRODUCTOS
    tree.column("# 1", anchor=CENTER, width= 60)
    tree.heading("# 1", text="Producto")
    tree.column("# 2", anchor=CENTER, width= 60)
    tree.heading("# 2", text="Precio")
    tree.place(x=0,y=0)


    db = sql.DataBase('superpy.db')
    productos = db.select_all("producto","nombre,precio_venta")
    for producto in productos:
    # Insert the data in Treeview widget
        tree.insert('','end', text="1",values=((producto[0], producto[1])))
    
    treeScroll = ttk.Scrollbar(ventana_catalogo)
    treeScroll.configure(orient="vertical",command=tree.yview)
    tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.place(x=100,y=0, height=100)



    ventana_catalogo.mainloop()