import tkinter
from tkinter import *
from Database import sql
#from Gui.tk_Carrito import carrito

def catalogo():
    ventana_catalogo = tkinter.Toplevel()
    ventana_catalogo.geometry("800x400")
    ventana_catalogo.title("Catalogo de Productos")
    ventana_catalogo.configure(bg = "blue4")
    
    #catalogo_productos = []

    db = sql.DataBase("superpy.db")
    # HAY QUE RECORRER LA LISTA, SEGURAMENTE CON i Y j. Como hago para saber hasta donde ponerles los limites?
    #a cada parametro?
    producto_valido = db.select_all("producto","nombre,precio_venta")

    


    #DEFICINION DE WIDGETS
    #atras_boton = tkinter.Button(ventana_catalogo, text = "ATRAS", command = carrito)
    catalogo_lista_producto = tkinter.Listbox(ventana_catalogo)
    catalogo_lista_precio = tkinter.Listbox(ventana_catalogo)

    for producto in producto_valido:
        catalogo_lista_producto.insert(END, producto[0])

    for producto in producto_valido:
        catalogo_lista_precio.insert(END, producto[1])

    #WIDGETS EN PANTALLA

    #atras_boton.grid(row = 1, column = 1)
    catalogo_lista_producto.grid(row = 2, column = 2)
    catalogo_lista_precio.grid(row = 2, column = 3)
    ventana_catalogo.mainloop()