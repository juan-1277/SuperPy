import tkinter
ventana_carrito = tkinter.Tk()
ventana_carrito.geometry("800x400")
ventana_carrito.title("Carro de compras")
ventana_carrito.configure(bg = "green")

#Creaciòn de Widgets
titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
total_label = tkinter.Label(ventana_carrito, text = "TOTAL A PAGAR $")
lista_label = tkinter.Label(ventana_carrito, text = "LISTA DE PRODUCTOS")
agregar_boton = tkinter.Button(ventana_carrito, text = "AGREGAR")
buscar_label = tkinter.Label(ventana_carrito , text = "Buscar un producto")
buscar_entry = tkinter.Entry(ventana_carrito)

#Colocaciòn de Widgets en pantalla
titulo_label.grid(row = 0, column = 3)
total_label.grid(row = 1, column = 20)
lista_label.grid(row = 3, column = 1)
buscar_label.grid(row = 4, column = 5)
buscar_entry.grid(row = 4, column = 8)
agregar_boton.grid(row = 4, column = 20)









ventana_carrito.mainloop()