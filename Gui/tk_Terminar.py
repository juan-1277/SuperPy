import tkinter
from tkinter import *
from Gui.tk_Carrito import *


def terminar():
    ventana_terminar = tkinter.Toplevel()
    ventana_terminar.geometry("800x400")
    ventana_terminar.title("Ventana Principal")
    ventana_terminar.configure(bg = "dark green")
    

    pagar = tkinter.Label(ventana_terminar, text = total_monto_label)
    pagar.grid(row = 1, column = 1)
   
