import tkinter
from tkinter import *
from Database import sql
from tkinter import ttk

def ventas():
    ventana_ventas= tkinter.Tk() 
    ventana_ventas.geometry("600x400")
    ventana_ventas.title("Informacion relevante para el producto")
    ventana_ventas.configure(bg = "blue4")     
        
    tree_ventas = ttk.Treeview(ventana_ventas, column = ("IDD venta","Tipo de Comprobante","N° de Comprobante","Fecha","Total", "Estado"), show='headings',height=4)

    # Add a Treeview widget CORRESPONDE AL TREEVIEW DE LOS PRODUCTOS
    tree_ventas.column("# 1", anchor=CENTER, width= 60)
    tree_ventas.heading("# 1", text="ID Venta")
    tree_ventas.column("# 2", anchor=CENTER, width= 120)
    tree_ventas.heading("# 2", text="Tipo de Comprobante")
    tree_ventas.column("# 3", anchor=CENTER, width= 150)
    tree_ventas.heading("# 3", text="N° de Comprobante")
    tree_ventas.column("# 4", anchor=CENTER, width= 60)
    tree_ventas.heading("# 4", text="Fecha")
    tree_ventas.column("# 5", anchor=CENTER, width= 60)
    tree_ventas.heading("# 5", text="Total")
    tree_ventas.column("# 6", anchor=CENTER, width= 60)
    tree_ventas.heading("# 6", text="Estado")

    presentacion_ventas=tkinter.Label(ventana_ventas,text="Resumen de Ventas")
    

    presentacion_ventas.grid(row=0,column=1)
    tree_ventas.grid(row=3,column=1)

    db = sql.DataBase("superpy.db")
    ventas = db.select_all("venta","id_venta,tipo_comprobante,nro_comprobante,fecha,total,estado")

    for venta in ventas:
        tree_ventas.insert('','end', text="1",values=((venta[0], venta[1], venta[2], venta[3], venta[4], venta[5])))     
    
    ventana_ventas.mainloop()

