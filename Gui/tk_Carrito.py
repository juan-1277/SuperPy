import tkinter
from tkinter import *
from Database import sql
from tkinter import messagebox
from Gui.tk_Catalogo import catalogo
from tkinter.font import Font
from tkinter import ttk
from datetime import date
from tkinter import messagebox

def carrito():    
    ventana_carrito = tkinter.Tk() #eliminar toplevel
    ventana_carrito.geometry("900x600")
    ventana_carrito.title("Carro de compras")
    ventana_carrito.configure(bg = "blue4")
    
    #DEFINICION DE FUNCIONES    
    global total_monto_label #ELIMINAR      
    
    def agregar_productosycantidades(producto):
        global resultado_total
        lista_productos.config(state="normal") #ACTIVA EL CAMPO PARA PODER HACER EL INGRESO
        lista_cantidades.config(state="normal") #ACTIVA EL CAMPO PARA PODER HACER EL INGRESO
        lista_parciales.config(state="normal")  #ACTIVA EL CAMPO PARA PODER HACER EL INGRESO
        total_monto_label.config(state="normal")

        if buscar(producto) == True:
            lista_productos.insert(END, txt_producto.get())           
            lista_cantidades.insert(END, cantidad_entry.get())                      
            db = sql.DataBase("superpy.db")
            precio_venta = db.select("producto","precio_venta", f"nombre = '{txt_producto.get()}'")
            resultado = 0
            resultado_total = 0            
            resultado = resultado + float(precio_venta[0][0])*float(cantidad_entry.get())
            lista_parciales.insert(END, resultado)                        
            resultado_total = resultado_total + resultado
            total = float(total_monto_label.get()) + float(precio_venta[0][0])*float(cantidad_entry.get())
            total_monto_label.delete(0,END)
            total_monto_label.insert(0,total)         

           #EN ESTE SECTOR SE DESACTIVA LOS CAMPOS.
            lista_productos.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
            lista_cantidades.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
            lista_parciales.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
            total_monto_label.config(state="disabled")

    def eliminar_productosycantidades():#ESTA FUNCION PERMITE ELIMINAR PRODUCTOS Y CANTIDADES AL MISMO TIEMPO
        indice = int(eliminar_entry.get())
        lista_productos.config(state="normal") #ACTIVA EL CAMPO PARA PODER ELIMINAR
        lista_cantidades.config(state="normal") #ACTIVA EL CAMPO PARA PODER ELIMINAR
        lista_parciales.config(state="normal")  #ACTIVA EL CAMPO PARA PODER ELIMINAR
        total_monto_label.config(state="normal")
        
        lista_productos.delete(indice - 1)#ESTE CODIGO ELIMINA EL ITEM "INDICE-1" DE LA LISTA
        lista_cantidades.delete(indice - 1)#ESTE CODIGO ELIMINA EL ITEM "INDICE-1" DE LA LISTA
        
        montoeliminado = lista_parciales.get(indice - 1) #1º) DESIGNA EL VALOR A ELIMINAR COMO MONTOELIMINADO
        total = float(total_monto_label.get()) - float(montoeliminado) #2º) SE UTILIZA EL MONTO ELIMINADO ANTERIOR PARA HACER LA RESTA
    
        total_monto_label.delete(0,END)#NUEVO
        total_monto_label.insert(0,total)   #NUEVO        

        lista_parciales.delete(indice - 1) #3º) RECIEN AHORA SE PROCEDE A ELIMINAR DICHO MONTO

        lista_productos.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
        lista_cantidades.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
        lista_parciales.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
        total_monto_label.config(state="disabled")#GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO


    def buscar(producto):
        db = sql.DataBase("superpy.db") 
        print(producto)       
        producto_valido = db.select("producto","nombre,precio_venta", f"nombre = '{producto}'")
                
        if len(producto_valido) > 0:       
            if producto == producto_valido[0][0]:
                messagebox.showinfo("Encontrado", "El producto existe")                                
                db.close() 
                return True
                
            else:
                messagebox.showinfo("No encontrado", "El producto NO existe")
                return False
        else:
            messagebox.showinfo("Producto no valido", "Ingrese un producto válido")
            return False
            
    ##CREACION DE WIDGETS  
    titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
    total_label = tkinter.Label(ventana_carrito, text = "Total a pagar $")
    total_monto_label = tkinter.Entry(ventana_carrito)
    total_monto_label.insert(0,"0.0")
    total_monto_label.config(state="disabled")
    lista_label = tkinter.Label(ventana_carrito, text = "Lista de productos")
    cantidades_label = tkinter.Label(ventana_carrito, text = "Cantidades")
    label_parciales = tkinter.Label(ventana_carrito, text = "Monto Parcial")
    agregar_producto_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = lambda: agregar_productosycantidades(txt_producto.get()), bg = "medium orchid")
    ingresar_label = tkinter.Label(ventana_carrito , text = "Ingresar un producto")
    cantidad_label = tkinter.Label(ventana_carrito , text = "Ingresar cantidad")
    cantidad_entry = tkinter.Spinbox(ventana_carrito, from_=0, to=1000, increment=1)
    txt_producto = tkinter.Entry(ventana_carrito)
    buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR", bg = "gray64", command = lambda: buscar(txt_producto.get())) 
    lista_productos = tkinter.Listbox(ventana_carrito)
    lista_cantidades = tkinter.Listbox(ventana_carrito)
    lista_parciales = tkinter.Listbox(ventana_carrito) #AGREGADO    
    eliminar_label = tkinter.Label(ventana_carrito, text = "Posición a eliminar")
    eliminar_entry = tkinter.Spinbox(ventana_carrito, from_=0, to=1000, increment=1)   
    eliminar_boton = tkinter.Button(ventana_carrito, text = "ELIMINAR", command = eliminar_productosycantidades, bg = "red")
    catalogo_boton = tkinter.Button(ventana_carrito, text = "CATALOGO", command = catalogo, bg = "SkyBlue1")
    terminar_boton = tkinter.Button(ventana_carrito, text = "TERMINAR", command = terminar)
    catalogo_tree = ttk.Treeview(ventana_carrito, column = ("Catalogo Productos","Precios", "Stock"), show='headings', selectmode="browse")
    catalogo_tree.column("# 1", anchor=CENTER, width= 120)
    catalogo_tree.heading("# 1", text="Catalogo productos")
    catalogo_tree.column("# 2", anchor=CENTER, width= 60)
    catalogo_tree.heading("# 2", text="Precios")
    catalogo_tree.column("# 3", anchor=CENTER, width= 60)
    catalogo_tree.heading("# 3", text="Stock")

    #COLOCACION DE WIDGETS EN PANTALLA

    titulo_label.grid(row = 0, column = 3) #TITULO DE LA VENTADA
    total_label.grid(row = 1, column = 6) #TEXTO TOTAL A PAGAR
    total_monto_label.grid(row = 1, column= 7) #CAJA DONDE SE MUESTRA EL MONTO TOTAL A PAGAR

    lista_label.grid(row = 2, column = 1) #TEXTO "LISTA DE PRODUCTOS"
    cantidades_label.grid(row = 2, column = 2) #TEXTO "CANTIDADES"
    label_parciales.grid(row = 2, column = 3) #TEXTO "montos parciales"
    
    agregar_producto_boton.grid(row = 4, column = 8) #BOTON PARA AGREGAR PRODUCTO    
    buscar_boton.grid(row = 4, column = 7) #BOTON PARA BUSCAR

    ingresar_label.grid(row = 4, column = 5) #TEXTO INGRESAR PRODUCTO
    txt_producto.grid(row = 4, column = 6) #CAMPO PARA INGRESAR PRODUCTO

    cantidad_label.grid(row = 5, column = 5) #TEXTO INGRESAR CANTIDAD
    cantidad_entry.grid(row = 5, column = 6) #CAMPO PARA INGRESAR CANTIDAD
    
    lista_productos.grid(row = 5, column = 1) #LISTADO DE PRODUCTOS
    lista_cantidades.grid(row = 5, column = 2) #LISTADO DE CANTIDADES
    lista_parciales.grid(row = 5, column = 3) #LISTADO DE PRECIOS

    eliminar_label.grid(row = 10, column = 1) #TEXTO "INGRESE POSICION A ELIMINAR"
    eliminar_entry.grid(row = 10, column = 2) #CAJA PARA INGRESAR EL INDICE A ELIMINAR
    eliminar_boton.grid(row = 10, column = 3) #BOTON ELIMINAR
    catalogo_boton.grid(row = 9, column = 7) #BOTON DE CATALOGO

    terminar_boton.grid(row = 14, column = 10)
    catalogo_tree.place(x=0, y=330)

    #LISTA DE PRODUCTOS EN LA BASE DE DATOS
    db = sql.DataBase("superpy.db")
    producto_valido = db.select_all("producto","nombre,precio_venta,stock")
    
    for producto_val in producto_valido:
        catalogo_tree.insert('','end', text="1",values=((producto_val[0], producto_val[1], producto_val[2])))

    catalogo_treeScrollbar = ttk.Scrollbar(ventana_carrito)
    catalogo_treeScrollbar.configure(orient="vertical", command=catalogo_tree.yview)
    catalogo_tree.configure(yscrollcommand=catalogo_treeScrollbar.set)
    catalogo_treeScrollbar.place(x=0+230,y=330, height=225)

    ventana_carrito.mainloop()

def terminar():
    ventana_terminar = tkinter.Toplevel()
    ventana_terminar.geometry("800x400")
    ventana_terminar.title("Ventana Principal")
    ventana_terminar.configure(bg = "blue4")    

    pagar = tkinter.Entry(ventana_terminar, font=Font(size=15))
    pagar.config(state="normal")
    pagar.insert(0,total_monto_label.get()) 
    pagar.config(state="disabled")

    texto_gracias = tkinter.Label(ventana_terminar, text = "Muchas gracias por elegirnos", font=Font(size=15))
    texto_pagar = tkinter.Label(ventana_terminar, text = "Su monto total a pagar es de: $")
    finalizar_venta = tkinter.Button(ventana_terminar, text="FINALIZAR",command=finalizar)  

    #COLOCACION DE WIDGETS EN PANTALLA      
    pagar.place(x=200, y =100)
    texto_gracias.place(x=200, y=0)
    texto_pagar.place(x=0, y=100)
    finalizar_venta.place(x=0,y=200)
    ventana_terminar.mainloop()

def finalizar():
    ventana_finalizar = tkinter.Toplevel()
    ventana_finalizar.geometry("800x400")
    ventana_finalizar.title("Ventas")
    ventana_finalizar.configure(bg = "blue4")    
    
    def cargar_venta():        
        db = sql.DataBase("superpy.db") 
        if len(tipocomprobante_entry.get()) > 0 and len(comprobante_entry.get()) > 0 and len(fecha_entry.get()) > 0 and len(total_monto_label.get()) > 0 and len(cliente_entry.get()):
            db = sql.DataBase("superpy.db")
            db.insert('venta','tipo_comprobante,nro_comprobante,fecha,total,id_cliente', f'"{tipocomprobante_entry.get()}","{comprobante_entry.get()}","{fecha_entry.get()}","{total_monto_label.get()}","{cliente_entry.get()}"')
            messagebox.showinfo("Agregado", "Venta generada.")
            db.close()  
        else:
            messagebox.showerror("ERROR", "Algo salió mal, la venta no se ha generado .")

    #DEFINICION DE WIDGETS
    tipocomprobante_label = tkinter.Label(ventana_finalizar, text = "Ingrese el tipo de comprobante")
    tipocomprobante_entry=tkinter.Entry(ventana_finalizar)
    comprobante_label = tkinter.Label(ventana_finalizar, text = "Ingrese n° de comprobante")
    comprobante_entry=tkinter.Entry(ventana_finalizar)
    cliente_label=tkinter.Label(ventana_finalizar, text="Ingrese el nombre y apellido del cliente: ")
    cliente_entry=tkinter.Entry(ventana_finalizar)
    fecha = tkinter.Label(ventana_finalizar, text = "Fecha")
    fecha_entry = tkinter.Entry(ventana_finalizar)
    dia = date.today()    
    fecha_entry.insert(END,dia)
    print(fecha_entry)
    total_entry = tkinter.Entry(ventana_finalizar)
    total_entry.insert(END, total_monto_label)
    cargar_venta_boton=tkinter.Button(ventana_finalizar,text= "CARGAR VENTA", command=cargar_venta)

    #COLOCACION DE WIDGETS EN PANTALLA
    tipocomprobante_label.grid(row=1,column=1)
    tipocomprobante_entry.grid(row=1,column=2)
    comprobante_label.grid(row=2,column=1)
    comprobante_entry.grid(row=2,column=2)
    fecha.grid(row=3,column=1)
    fecha_entry.grid(row=3,column=2)
    cliente_label.grid(row=4,column=1)
    cliente_entry.grid(row=4,column=2)
    cargar_venta_boton.grid(row=5,column=1)    
    
    ventana_finalizar.mainloop()




