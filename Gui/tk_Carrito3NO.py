import tkinter
from tkinter import *
from Database import sql
from tkinter import messagebox
from Gui.tk_Catalogo import catalogo
from tkinter.font import Font
#from Gui.tk_Terminar import terminar #ELIMINAR


def carrito():    
    ventana_carrito = tkinter.Tk() #eliminar toplevel
    ventana_carrito.geometry("1080x720")
    ventana_carrito.title("Carro de compras")
    ventana_carrito.configure(bg = "blue4")
    #resultado = 0 
    #DEFINICION DE FUNCIONES
    #global resultado_total
    ##resultado = StringVar()
    ##precio_venta = int()
    global total_monto_label #ELIMINAR
        
        
    
    def agregar_productosycantidades(producto):
        global resultado_total
        lista_productos.config(state="normal") #ACTIVA EL CAMPO PARA PODER HACER EL INGRESO
        lista_cantidades.config(state="normal") #ACTIVA EL CAMPO PARA PODER HACER EL INGRESO
        lista_parciales.config(state="normal")  #ACTIVA EL CAMPO PARA PODER HACER EL INGRESO

        #resultado_total = 0
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
           
            lista_productos.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
            lista_cantidades.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
            lista_parciales.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
    

  #  def itemseleccionado(): #ELIMINAR NO FUNCIONA
   #     for item in catalogo_lista_producto():
    #        LB = tkinter.Label(ventana_carrito, text = catalogo_lista_producto.get(item)).pack()



    def eliminar_productosycantidades():#ESTA FUNCION PERMITE ELIMINAR PRODUCTOS Y CANTIDADES AL MISMO TIEMPO
        indice = int(eliminar_entry.get())
        lista_productos.config(state="normal") #ACTIVA EL CAMPO PARA PODER ELIMINAR
        lista_cantidades.config(state="normal") #ACTIVA EL CAMPO PARA PODER ELIMINAR
        lista_parciales.config(state="normal")  #ACTIVA EL CAMPO PARA PODER ELIMINAR

        lista_productos.delete(indice - 1)
        lista_cantidades.delete(indice - 1)
        #lista_parciales.delete(indice - 1) ELIMINAR
        
        #montoeliminado = lista_cantidades.delete(indice - 1) ELIMINAR
        #print(montoeliminado)    ELIMINAR
        #lista_parciales.delete(indice - 1) #ELIMINAR

        montoeliminado = lista_parciales.get(indice - 1) #1º) DESIGNA EL VALOR A ELIMINAR COMO MONTOELIMINADO
        
        total = float(total_monto_label.get()) - float(montoeliminado) #2º) SE UTILIZA EL MONTO ELIMINADO ANTERIOR PARA HACER LA RESTA
        
        total_monto_label.delete(0,END)#NUEVO
        total_monto_label.insert(0,total)   #NUEVO
        

        lista_parciales.delete(indice - 1) #3º) RECIEN AHORA SE PROCEDE A ELIMINAR DICHO MONTO

        lista_productos.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
        lista_cantidades.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO
        lista_parciales.config(state="disabled") #GRISA EL CAMPO PARA VOLVER A DEJARLO BLOQUEADO HASTA EL PROXIMO EVENTO



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

            
    #def buscar(producto): 
            #db = sql.DataBase("superpy.db")
            #producto_valido = db.select("usuario", "email,password",f'email = {email}',f'password = {password}')

        # if email == usuario_valido[0][0]:
            #    if password == usuario_valido[0][1]:
            #       tkinter.messagebox.showinfo(title="Inicio", message="Inicio de sesión exitoso")
            #db.close() #siempre cerrar la conexión a la base de datos

    







    ##CREACION DE WIDGETS
    
    
    
    #producto = StringVar()
    titulo_label = tkinter.Label(ventana_carrito, text = "Carro de compras")
    total_label = tkinter.Label(ventana_carrito, text = "Total a pagar $")
    total_monto_label = tkinter.Entry(ventana_carrito)
    total_monto_label.insert(0,"0.0")

    lista_label = tkinter.Label(ventana_carrito, text = "Lista de productos")
    cantidades_label = tkinter.Label(ventana_carrito, text = "Cantidades")
    label_parciales = tkinter.Label(ventana_carrito, text = "Monto Parcial")

    agregar_producto_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = lambda: agregar_productosycantidades(txt_producto.get()), bg = "SkyBlue1")
    #agregar_producto_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = itemseleccionado)
    
    #agregar_cantidad_boton = tkinter.Button(ventana_carrito, text = "AGREGAR Q", command = agregar_cantidad)
    ingresar_label = tkinter.Label(ventana_carrito , text = "Ingresar un producto")
    cantidad_label = tkinter.Label(ventana_carrito , text = "Ingresar cantidad")
    cantidad_entry = tkinter.Spinbox(ventana_carrito)
    #txt_producto = tkinter.Entry(ventana_carrito, textvariable = producto)
    txt_producto = tkinter.Entry(ventana_carrito)
    buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR", bg = "gray64", command = lambda: buscar(txt_producto.get()))
    
    lista_productos = tkinter.Listbox(ventana_carrito)
    lista_cantidades = tkinter.Listbox(ventana_carrito)
    lista_parciales = tkinter.Listbox(ventana_carrito) #AGREGADO
    
    eliminar_label = tkinter.Label(ventana_carrito, text = "Posición a eliminar")
    eliminar_entry = tkinter.Spinbox(ventana_carrito)   
    eliminar_boton = tkinter.Button(ventana_carrito, text = "ELIMINAR", command = eliminar_productosycantidades, bg = "red")
    
    catalogo_boton = tkinter.Button(ventana_carrito, text = "CATALOGO", command = catalogo, bg = "SkyBlue1")

    terminar_boton = tkinter.Button(ventana_carrito, text = "TERMINAR", command = terminar)

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





    #####
    db = sql.DataBase("superpy.db")
    # HAY QUE RECORRER LA LISTA, SEGURAMENTE CON i Y j. Como hago para saber hasta donde ponerles los limites?
    #a cada parametro?
    producto_valido = db.select_all("producto","nombre,precio_venta")


    catalogo_productos = tkinter.Label(ventana_carrito, text = "Catalogo de productos")
    precios_productos = tkinter.Label(ventana_carrito, text = "Precios unitarios")

    catalogo_lista_producto = tkinter.Listbox(ventana_carrito)# LISTA DE PRODUCTOS EN CATALOGO
    
    catalogo_lista_precio = tkinter.Listbox(ventana_carrito)#LISTA DE PRECIOS EN CATALOGO

    for producto in producto_valido:
        catalogo_lista_producto.insert(END, producto[0])

    for producto in producto_valido:
        catalogo_lista_precio.insert(END, producto[1])


    catalogo_lista_producto.config(state="disabled") #ESTO PERMITE GRISAR LA LISTA DE CATALOGOS
    catalogo_lista_precio.config(state="disabled")  #ESTO PERMITE GRISAR LA LISTA DE CATALOGOS

    
    #WIDGETS EN PANTALLA

    #atras_boton.grid(row = 1, column = 1)
    catalogo_lista_producto.grid(row = 13, column = 1)
    catalogo_lista_precio.grid(row = 13, column = 2)
    catalogo_productos.grid(row = 12, column = 1)
    precios_productos.grid(row = 12, column = 2)


  


    ventana_carrito.mainloop()




def terminar():
    ventana_terminar = tkinter.Toplevel()
    ventana_terminar.geometry("800x400")
    ventana_terminar.title("Ventana Principal")
    ventana_terminar.configure(bg = "dark green")
    

    pagar = tkinter.Entry(ventana_terminar, font=Font(size=15))
    pagar.config(state="normal")
    pagar.insert(0,total_monto_label.get()) 
    pagar.config(state="disabled")

    texto_gracias = tkinter.Label(ventana_terminar, text = "Muchas gracias por elegirnos", font=Font(size=15))
    texto_pagar = tkinter.Label(ventana_terminar, text = "Su monto total a pagar es de: $")


          
    pagar.place(x=200, y =100)
    texto_gracias.place(x=200, y=0)
    texto_pagar.place(x=0, y=100)
    ventana_terminar.mainloop()