import tkinter
from tkinter import *

#DEFINICION DE LA VENTANA
ventana_carrito = tkinter.Tk()
ventana_carrito.geometry("800x400")
ventana_carrito.title("Carro de compras")
ventana_carrito.configure(bg = "green")

#DEFINICION DE VARIABLES
producto = StringVar()

#DEFINICION DE FUNCIONES
#def agregar_productos():
  # lista_productos.insert(END, producto.get())
   #lista_productos = list()

#Creaciòn de Widgets
titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
total_label = tkinter.Label(ventana_carrito, text = "TOTAL A PAGAR $")
lista_label = tkinter.Label(ventana_carrito, text = "LISTA DE PRODUCTOS")
agregar_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = agregar_productos)
buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR")
buscar_label = tkinter.Label(ventana_carrito , text = "Buscar un producto")
txt_producto = tkinter.Entry(ventana_carrito, textvariable = producto)
lista_productos = tkinter.Listbox(ventana_carrito)
# Marco para contener el listbox y la barra de desplazamiento.
frame = tkinter.Frame()
# Crear una barra de deslizamiento con orientación vertical.
scrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
# Vincularla con la lista.
lista_productos = tkinter.Listbox(frame,yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_productos.yview)
# Ubicarla a la derecha.


#Colocaciòn de Widgets en pantalla
titulo_label.grid(row = 0, column = 3)
total_label.grid(row = 1, column = 20)
lista_label.grid(row = 3, column = 1)
buscar_label.grid(row = 4, column = 5)
txt_producto.grid(row = 4, column = 8)
agregar_boton.grid(row = 4, column = 20)
buscar_boton.grid(row = 5, column = 20)
lista_productos.grid(row = 5, column = 1)
scrollbar.grid(row = 7, column = 7)
frame.grid(row = 7, column = 1)





ventana_carrito.mainloop()