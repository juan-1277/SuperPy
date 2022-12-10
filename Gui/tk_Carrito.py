import tkinter
from tkinter import *


ventana_carrito = tkinter.Tk()
ventana_carrito.geometry("800x400")
ventana_carrito.title("Carro de compras")
ventana_carrito.configure(bg = "green")
producto = StringVar()

#Definicion de funciones
def agregar_productos():
   lista_productos.insert(END, producto.get())
#lista_productos = list()

def agregar_cantidad():
    lista_cantidades.insert(END, cantidad_entry.get())

def eliminar_productos(item):
    lista_productos.delete(item)

#Creaciòn de Widgets
titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
total_label = tkinter.Label(ventana_carrito, text = "Total a pagar $")
lista_label = tkinter.Label(ventana_carrito, text = "Lista de productos")
cantidades_label = tkinter.Label(ventana_carrito, text = "Cantidades")
agregar_producto_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = agregar_productos)
agregar_cantidad_boton = tkinter.Button(ventana_carrito, text = "AGREGAR Q", command = agregar_cantidad)
buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR")
ingresar_label = tkinter.Label(ventana_carrito , text = "Ingresar un producto")
cantidad_label = tkinter.Label(ventana_carrito , text = "Ingresar cantidad")
cantidad_entry = tkinter.Spinbox(ventana_carrito)
txt_producto = tkinter.Entry(ventana_carrito, textvariable = producto)
lista_productos = tkinter.Listbox(ventana_carrito)
lista_cantidades = tkinter.Listbox(ventana_carrito)
eliminar_label = tkinter.Label(ventana_carrito, text = "Pos. a Eliminar")
eliminar_entry = tkinter.Spinbox(ventana_carrito)
eliminar_boton = tkinter.Button(ventana_carrito, text = "ELIMINAR", command = eliminar_productos)


#Colocaciòn de Widgets en pantalla
titulo_label.grid(row = 0, column = 3)
total_label.grid(row = 1, column = 6)
lista_label.grid(row = 2, column = 1)
cantidades_label.grid(row = 2, column = 2)
agregar_producto_boton.grid(row = 4, column = 7)
agregar_cantidad_boton.grid(row = 5, column = 6)
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