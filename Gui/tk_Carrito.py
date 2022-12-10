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
lista_productos = list()

def eliminar_productos(posicion):
    lista_productos.delete(posicion)

#Creaciòn de Widgets
titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
total_label = tkinter.Label(ventana_carrito, text = "TOTAL A PAGAR $")
lista_label = tkinter.Label(ventana_carrito, text = "LISTA DE PRODUCTOS")
agregar_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = agregar_productos)
buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR")
buscar_label = tkinter.Label(ventana_carrito , text = "Ingresar un producto")
txt_producto = tkinter.Entry(ventana_carrito, textvariable = producto)
lista_productos = tkinter.Listbox(ventana_carrito)
eliminar_label = tkinter.Label(ventana_carrito, text = "Pos. a Eliminar")
eliminar_entry = tkinter.Entry(ventana_carrito)
eliminar_boton = tkinter.Button(ventana_carrito, text = "ELIMINAR", command = eliminar_productos(eliminar_entry +1))


#Colocaciòn de Widgets en pantalla
titulo_label.grid(row = 0, column = 3)
total_label.grid(row = 1, column = 10)
lista_label.grid(row = 2, column = 1)
buscar_label.grid(row = 4, column = 3)
txt_producto.grid(row = 4, column = 8)
agregar_boton.grid(row = 4, column = 12)
buscar_boton.grid(row = 4, column = 10)
lista_productos.grid(row = 5, column = 1)
eliminar_label.grid(row = 7, column = 1)
eliminar_entry.grid(row = 7, column = 2)
eliminar_boton.grid(row = 7, column = 3)




ventana_carrito.mainloop()