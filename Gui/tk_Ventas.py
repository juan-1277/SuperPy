import tkinter
from tkinter import *
from Database import sql
from tkinter import ttk

def ventas():
    ventana_ventas= tkinter.Tk() 
    ventana_ventas.geometry("1200x800")
    ventana_ventas.title("Informacion relevante para el producto")
    ventana_ventas.configure(bg = "blue4")     
        
    tree_ventas = ttk.Treeview(ventana_ventas, column = ("ID venta","ID Cliente","Tipo de Comprobante","N° de Comprobante","fecha","Total", "Estado", "ID usuario"), show='headings')

    # Add a Treeview widget CORRESPONDE AL TREEVIEW DE LOS PRODUCTOS
    tree_ventas.column("# 1", anchor=CENTER, width= 60)
    tree_ventas.heading("# 1", text="ID Venta")
    tree_ventas.column("# 2", anchor=CENTER, width= 60)
    tree_ventas.heading("# 2", text="ID Cliente")
    tree_ventas.column("# 3", anchor=CENTER, width= 150)
    tree_ventas.heading("# 3", text="Tipo de Comprobante")
    tree_ventas.column("# 4", anchor=CENTER, width= 200)
    tree_ventas.heading("# 4", text="N° de Comprobante")
    tree_ventas.column("# 5", anchor=CENTER, width= 60)
    tree_ventas.heading("# 5", text="Fecha")
    tree_ventas.column("# 6", anchor=CENTER, width= 60)
    tree_ventas.heading("# 6", text="Total")
    tree_ventas.column("# 7", anchor=CENTER, width= 60)
    tree_ventas.heading("# 7", text="Estado")
    tree_ventas.column("# 8", anchor=CENTER, width= 60)
    tree_ventas.heading("# 8", text="ID usuario")

    db = sql.DataBase("superpy.db")
    ventas = db.select_all("venta","id_venta,id_cliente,tipo_comprobante,nro_comprobante,fecha,total,estado,id_usuario")

    for venta in ventas:
        tree_ventas.insert('','end', text="1",values=((venta[0], venta[1], venta[2], venta[3], venta[4], venta[5],venta[6],venta[7])))   
    db.close()
    presentacion_ventas=tkinter.Label(ventana_ventas,text="Resumen de Ventas")
    tree_ventas=ttk.Treeview(ventana_ventas)

    presentacion_ventas.grid(row=0,column=4)
    tree_ventas.grid(row=3,column=1)
    
    ventana_ventas.mainloop()

