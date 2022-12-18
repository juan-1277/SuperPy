import tkinter
from tkinter import *
from Database import sql
from tkinter import messagebox
from Gui.tk_Productos import catalogo




def carrito():    
    ventana_carrito = tkinter.Tk()
    ventana_carrito.geometry("800x800")
    ventana_carrito.title("Carro de compras")
    ventana_carrito.configure(bg = "blue4")
    #resultado = 0 
    #DEFINICION DE FUNCIONES
    #global resultado_total
    ##resultado = StringVar()
    ##precio_venta = int()
    
    def agregar_productosycantidades(producto):
        global resultado_total
        #resultado_total = 0
        if buscar(producto) == True:
            lista_productos.insert(END, txt_producto.get())
            lista_cantidades.insert(END, cantidad_entry.get())
            
            db = sql.DataBase("superpy.db")
            precio_venta = db.select("producto","precio_venta", f"nombre = '{txt_producto.get()}'")
            resultado = 0
            resultado_total = 0
            
            resultado = resultado + float(precio_venta[0][0])*float(cantidad_entry.get())
            lista_precios.insert(END, resultado)
            #total_monto_label.insert(0,resultado)
            resultado_total = resultado_total + resultado
            total_monto_label.insert(0,resultado_total)            
            #print(resultado_total)                  
        
            

    def eliminar_productosycantidades():#ESTA FUNCION PERMITE ELIMINAR PRODUCTOS Y CANTIDADES AL MISMO TIEMPO
        indice = int(eliminar_entry.get())
        lista_productos.delete(indice - 1)
        lista_cantidades.delete(indice - 1)

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
    lista_label = tkinter.Label(ventana_carrito, text = "Lista de productos")
    cantidades_label = tkinter.Label(ventana_carrito, text = "Cantidades")
    #precio_venta_label = tkinter.Label(ventana_carrito, text = "Precio")
    agregar_producto_boton = tkinter.Button(ventana_carrito, text = "AGREGAR", command = lambda: agregar_productosycantidades(txt_producto.get()), bg = "SkyBlue1")
    #agregar_cantidad_boton = tkinter.Button(ventana_carrito, text = "AGREGAR Q", command = agregar_cantidad)
    ingresar_label = tkinter.Label(ventana_carrito , text = "Ingresar un producto")
    cantidad_label = tkinter.Label(ventana_carrito , text = "Ingresar cantidad")
    cantidad_entry = tkinter.Spinbox(ventana_carrito)
    #txt_producto = tkinter.Entry(ventana_carrito, textvariable = producto)
    txt_producto = tkinter.Entry(ventana_carrito)
    buscar_boton = tkinter.Button(ventana_carrito, text = "BUSCAR", bg = "gray64", command = lambda: buscar(txt_producto.get()))
    lista_productos = tkinter.Listbox(ventana_carrito)
    lista_cantidades = tkinter.Listbox(ventana_carrito)
    lista_precios = tkinter.Listbox(ventana_carrito) #AGREGADO
    eliminar_label = tkinter.Label(ventana_carrito, text = "Posición a eliminar")
    eliminar_entry = tkinter.Spinbox(ventana_carrito)   
    eliminar_boton = tkinter.Button(ventana_carrito, text = "ELIMINAR", command = eliminar_productosycantidades, bg = "red")
    catalogo_boton = tkinter.Button(ventana_carrito, text = "CATALOGO", command = catalogo, bg = "SkyBlue1")

    #COLOCACION DE WIDGETS EN PANTALLA

    titulo_label.grid(row = 0, column = 3)
    total_label.grid(row = 1, column = 6)
    total_monto_label.grid(row = 1, column= 7)
    lista_label.grid(row = 2, column = 1)
    cantidades_label.grid(row = 2, column = 2)
    #precio_venta_label.grid()
    agregar_producto_boton.grid(row = 4, column = 7)
    #agregar_cantidad_boton.grid(row = 5, column = 6)
    buscar_boton.grid(row = 4, column = 6)
    ingresar_label.grid(row = 4, column = 3)
    cantidad_label.grid(row = 5, column = 3)
    cantidad_entry.grid(row = 5, column = 5)
    txt_producto.grid(row = 4, column = 5)
    lista_productos.grid(row = 5, column = 1)
    lista_cantidades.grid(row = 5, column = 2)
    lista_precios.grid(row = 9, column = 1) #AGREGADO
    eliminar_label.grid(row = 7, column = 1)
    eliminar_entry.grid(row = 7, column = 2)
    eliminar_boton.grid(row = 7, column = 3)
    catalogo_boton.grid(row = 8, column = 7)



    ventana_carrito.mainloop()