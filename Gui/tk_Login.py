import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")

boton1 = tkinter.Button(ventana, text = "Productos", bg = "orange")
boton1.pack()

boton2 = tkinter.Button(ventana, text = "Usuarios", bg = "orange")
boton2.pack()

boton3 = tkinter.Button(ventana, text = "Ventas", bg = "orange")
boton3.pack()

boton4 = tkinter.Button(ventana, text = "Salir", bg = "orange")
boton4.pack()


ventana.mainloop()