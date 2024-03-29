from Database import sql
from Proyecto.producto import Producto
from Proyecto.cliente import Cliente
from Proyecto.detalle_venta import DetalleVenta
from Login.usuario import Usuario
from datetime import datetime

class Venta:

    def __init__(self, cliente = 0, tipo_comprobante="", nro_comprobante="", fecha="", total=0.0, detalle=[],id_venta = 0):
        self.__cliente = cliente
        self.__fecha = fecha
        self.__total = total
        self.__detalle = detalle
        self.__tipoComprobante = tipo_comprobante
        self.__nro_comprobante = nro_comprobante
        self.__idventa = id_venta
    
    @property
    def Cliente(self):
        return self.__cliente
    
    @Cliente.setter
    def Cliente(self, cliente):
        self.__cliente = cliente
    
    @property
    def Fecha(self):
        return self.__fecha
    
    @Fecha.setter
    def Fecha(self, fecha):
        self.__fecha = fecha
    
    @property
    def Total(self):
        return self.__total
    
    @Total.setter
    def Total(self, total):
        self.__total = total
    
    @property
    def Detalle(self):
        return self.__detalle
    
    @Detalle.setter
    def Detalle(self, detalle):
        self.__detalle = detalle
    
    @property
    def TipoComprobante(self):
        return self.__tipoComprobante
    
    @TipoComprobante.setter
    def TipoComprobante(self,tipo_comprobante):
        self.__tipoComprobante = tipo_comprobante
        
    @property
    def NroComprobante(self):
        return self.__nro_comprobante
    
    @NroComprobante.setter
    def NroComprobante(self,nro_comprobante):
        self.__nro_comprobante = nro_comprobante
        
    def __str__(self):
        return self.__cliente + " - " + self.__fecha + " - " + str(self.__total)
    
    
    def crearVenta(self):
        db = sql.DataBase("superpy.db")
        persona = Cliente()
        print("-------------------------------------------------")
        print("Seleccione un Cliente ")
        print("Si no encuentra al Cliente dar de Alta en cliente")
        persona.listarClientes()
        print("")
        self.__cliente = input("Ingrese el Nro de Cliente : ")
        print("-------------------------------------------------")
        print("")
        self.__tipoComprobante = input("Ingrese el Tipo de Comprobante : ")
        print("")
        self.__nro_comprobante = input("Ingrese N° Comprobante : ")
        print("")
        print("------------- Seleccione el Producto -------------")
        detalles=[]
        runnig = True
        while runnig:
            producto = Producto()
            producto.listarProducto()
            print("")
            while runnig:
                id_producto = int(input("Ingrese el Nro del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = db.select("producto","precio_venta",f"id_producto = {id_producto}")
                producto = db.select("producto","stock",f"id_producto = {id_producto} ")
                stock = producto[0][0]
                if stock == 0:
                    cantidad == 0
                else:
                    stock = stock - cantidad
                db.update("producto","stock",stock,f"id_producto = {id_producto} ")
                subtotal = precio[0][0] * cantidad
                detalles.append(DetalleVenta(id_producto, cantidad,subtotal))
                self.__total += subtotal 
                producto = db.select("producto","stock",f"id_producto = {id_producto} ")
                stock = producto[0][0]
                if stock == 0:
                    print("Producto sin stock")
                print("---------------------------------------------------")
                opcion = int(input("Desea Ingresar otros Productos?\n 1 - SI\n 0 - NO\n "))
                if opcion == 0:
                    runnig = False
                print("####################################################")
                self.__fecha = datetime.today().strftime('%Y-%m-%d')
                usuario =Usuario()
                id_usuario = usuario.usuario_id()
                db.insert("venta","id_cliente,tipo_comprobante,nro_comprobante,fecha,total,id_usuario",
                        f"'{self.__cliente}','{self.__tipoComprobante}','{self.__nro_comprobante}','{self.__fecha}','{self.__total}','{id_usuario}'")
                self.__idventa = db.get_last_id()
                for detalle in detalles:
                    db.insert("detalle_venta","id_venta,id_producto,cantidad,precio",
                        f"'{self.__idventa}','{detalle.idproducto}','{detalle.Cantidad}','{detalle.Subtotal}'")
        db.close()
        
    def anularVenta(self,id_venta):
        db = sql.DataBase("superpy.db")
        db.update("venta","estado",0,f"id_venta = {id_venta}")
        db.close()
        
    def borrarVenta(self,id_venta):
        producto = Producto()
        db = sql.DataBase("superpy.db")
        producto = db.select("detalle_venta","cantidad",f"id_venta = {id_venta}")
        cantidad = producto[0][0]
        ajuste_producto = db.select("detalle_venta","id_producto",f"id_venta = {id_venta}")
        id_producto = ajuste_producto[0][0]
        producto = db.select("producto","stock",f"id_producto = {id_producto} ")
        stock = producto[0][0]
        stock = stock + cantidad
        db.update("producto","stock",stock,f"id_producto = {id_producto} ")
        db.delete("venta",f"id_venta = {id_venta}")
        db.delete("detalle_venta",f"id_venta = {id_venta}")
        db.close()
    
    def all_venta(self):
        db = sql.DataBase("superpy.db")
        ventas = db.select_all("venta","id_venta,id_cliente,tipo_comprobante,nro_comprobante,fecha,total,estado,id_usuario")
        print("###############################################################")
        print("Nro\tCliente\t\tTipo Comprobante\tNumero Comprobante\tFecha\t\tTotal\t\tEstado\tUsuario")
        for venta in ventas:
            cliente = db.select("cliente","apellido|| ' ' ||nombre",f"id_cliente = {venta[1]}")
            print(f"{venta[0]}\t{cliente[0][0]}\t{venta[2]}\t\t{venta[3]}\t\t\t{venta[4]}\t{venta[5]}\t{venta[6]}\t{venta[7]}")
        print("################################################################")
        db.close()
        
    