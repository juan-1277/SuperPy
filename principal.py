from Proyecto.producto import Producto
from datetime import datetime,date

print("###########")
print("MENU")
print("###########")
runing = True
while runing:
    print("###########")
    print("Opciones")
    print("###########")
    #agregando las Opciones
    print("1 - Administracion")
    print("2 - Cliente")
    opcion = int(input("Elija opcion : "))
    
    if opcion == 1:
        print("1 - Crear un producto")
        print("2 - Mostrar todos los productos")
        print("3 - Modificar un producto") 
        print("4 - Eliminar un producto") 
        sub_opcion = int(input("Elija opcion : "))
        if sub_opcion == 1:
           codigo = input("Codigo del producto : ")
           nombre = input("Nombre del producto : ")
           precio_venta = float(input("Precio de venta del producto : "))
           stock = int(input("Stock del producto : "))
           descripcion = input("Descripcion del producto : ")
           producto = Producto(codigo,nombre,precio_venta,stock,descripcion)
           producto.create_producto()
        elif sub_opcion == 2:
           producto = Producto()
           print(producto.get_all_producto())
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
        elif sub_opcion == 4:
            producto = Producto()
            print("\tCodigo\tNombre\tPrecio_venta\tStock\tDescripcion")
            id = 1
            for prod in producto.get_all_producto():
               print(f"{id} -  {prod[0]}\t - {prod[1]} - {prod[2]}")
               id += 1 
            producto_select = input("Ingrese id del producto a eliminar : ")
            producto.delete_producto(producto_select)