import sys
print(sys.path)
from Proyecto.producto import Producto
from Login.rol import Rol
from Login.usuario import Usuario
from Proyecto.categoria import Categoria
from os import system
#from progress.bar import Bar
import time,random

""" login = True
system("cls")
while login:
    try:
        print("#####################################")
        print("##########    Login     #############")
        email = input("Email : ")
        password = input("Contraseña : ")
        usuario = Usuario()
        if (usuario.login(email,password)):
             login = False
        print("#####################################")
    except Exception as e :
        print(e + "Inicio de Session Incorrecto")
print("Has iniciado session XD")
bar = Bar('Cargando Sistema', max=100)
for num in range(100):
    time.sleep(random.uniform(0, 0.5))
    bar.next()
bar.finish()
system("cls") """

runing = True
while runing:
   print("#####################################")
   print("############## MENU #################")
   print("#####################################")
   runing = True
   while runing:
      print("")
      print("Opciones")
      print("")
      #agregando las Opciones
      print("1 - Productos")
      print("2 - Usuarios")
      print("3 - Ventas ")
      print("0 - Salir del Sistema ")
      print("")
      opcion = int(input("Elija opcion : "))
      if opcion == 1:
          sub_opcion = -1
          while sub_opcion != 0:
               system("cls")
               print("########################################")
               print("#############  PRODUCTOS  ##############")
               print("########################################")          
               print("1 - Crear un producto")
               print("2 - Mostrar todos los productos")
               print("3 - Modificar un producto") 
               print("4 - Eliminar un producto") 
               print("5 - Crear Categoria ")
               print("6 - Actualizar Categoria ")
               print("7 - Eliminar Categoria ")
               print("8 - Ver Todas las Categorias ")
               print("0 - Volver ")
               print("")
               sub_opcion = int(input("Elija opcion : "))
               print("")
               system("cls")
               if sub_opcion == 1:
                  codigo = input("Codigo del producto : ")
                  nombre = input("Nombre del producto : ")
                  precio_venta = float(input("Precio de venta del producto : "))
                  stock = int(input("Stock del producto : "))
                  descripcion = input("Descripcion del producto : ")
                  producto = Producto(codigo,nombre,precio_venta,stock,descripcion)
                  producto.crear_producto()
               elif sub_opcion == 2:
                  producto = Producto()
                  print(producto.get_all_producto())
                  volver = int(input("0 - Volver "))
               elif sub_opcion == 3:
                     producto = Producto()
                     print("\tCodigo\tNombre\tPrecio_venta\tStock\tDescripcion")
                     id = 1
                     for prod in producto.get_all_producto():
                        print(f"{id} -  {prod[0]}\t - {prod[1]} - {prod[2]}")
                     producto_select = input("Ingrese id del producto a actualizar : ")
                     codigo = input("Codigo del producto : ")
                     nombre = input("Nombre del producto : ")
                     precio_venta = float(input("Precio de venta del producto : "))
                     stock = int(input("Stock del producto : "))
                     descripcion = input("Descripcion del producto : ")
                     datos = {"codigo":codigo,"nombre":nombre,"precio_venta":precio_venta,"stock":stock, "descripcion":descripcion}
                     producto.update_producto(datos)
                     volver = int(input("0 - Volver "))
               elif sub_opcion == 4:
                     producto = Producto()
                     print("\tCodigo\tNombre\tPrecio_venta\tStock\tDescripcion")
                     id = 1
                     for prod in producto.get_all_producto():
                        print(f"{id} -  {prod[0]}\t - {prod[1]} - {prod[2]}")
                        id += 1 
                     producto_select = input("Ingrese id del producto a eliminar : ")
                     producto.delete_producto(producto_select)
                     volver = int(input("0 - Volver "))
               elif sub_opcion == 5:
                categoria = Categoria()
                categoria.create_categoria()
               elif sub_opcion == 6:
                  categoria = Categoria()
                  categoria.listar_categoria()
                  print("0 - Volver ")
                  id_categoria = int(input("Ingrese un numero de Categoria: "))
                  if id_categoria != 0:
                     categoria.update_categoria(id_categoria)
               elif sub_opcion == 7:
                  categoria = Categoria()
                  categoria.listar_categoria()
                  id_categoria = int(input("Ingrese un numero de Categoria: "))
                  if id_categoria != 0:
                     categoria.eliminar_categoria(id_categoria)
               elif sub_opcion == 8:
                  categoria = Categoria()
                  categoria.listar_categoria()
                  volver = int(input("0 - Volver "))
               else:
                  sub_opcion = 0
                
runing = False