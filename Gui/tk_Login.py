import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")

def close(): #corresponde a la funcion para cerrar la ventana Tkinter, invocada en el boton "Exit"
    ventana.destroy()

boton1 = tkinter.Button(ventana, text = "INGRESAR", bg = "orange")
boton1.pack()

boton_exit = tkinter.Button(ventana, text = "Exit", bg = "orange", command = close)
boton_exit.pack()

ventana.mainloop()