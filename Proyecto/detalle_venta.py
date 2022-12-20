from Database import sql


class DetalleVenta:

    def __init__(self,idproducto = 0, cantidad = 0,subtotal = 0.0,id_detalleVenta = 0, idventa = 0):
        self.__id_detalleVenta = id_detalleVenta
        self.__cantidad = cantidad
        self.__idproducto = idproducto
        self.__idventa = idventa
        self.__subtotal = subtotal
    
    @property
    def Id_detalleVenta(self):
        return self.__id_detalleVenta
    
    @Id_detalleVenta.setter
    def Id(self, id_detalleVenta):
        self.__id_detalleVenta = id_detalleVenta
    
    @property
    def idventa(self):
        return self.__idventa
    
    @idventa.setter
    def idventa(self, idventa):
        self.__idventa = idventa
    
    @property
    def idproducto(self):
        return self.__idproducto
    
    @idproducto.setter
    def idproducto(self, idproducto):
        self.__idproducto = idproducto
    
    @property
    def Cantidad(self):
        return self.__cantidad
    
    @Cantidad.setter
    def Cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    @property
    def Subtotal(self):
        return self.__subtotal
    
    @Subtotal.setter
    def Subtotal(self, subtotal):
        self.__subtotal = subtotal
    
    def __str__(self):
        return self.__cantidad + " - " + self.__idproducto

    def get_detalleventa(self,id_venta):
        db = sql.DataBase("superpy.db")
        venta = db.select("venta","id_venta,id_cliente,tipo_comprobante,nro_comprobante,fecha,total,id_usuario",
                    f"id_venta = {id_venta}")
        cliente = db.select("cliente","apellido|| ' ' ||nombre",f"id_cliente = {venta[0][1]}")
        usuario = db.select("usuario","apellido|| ' ' ||nombre",f"id_usuario = {venta[0][6]}")
        detalles = db.select("detalle_venta","id_venta,id_producto,cantidad,precio",
                             f"id_venta = {id_venta}")
        print('-------------------------------------------')
        print('             SUPERPY   ')
        print('-------------------------------------------')
        print('Tipo Comprobante : ',venta[0][2],'\tnumero_comprobante : ',venta[0][3])
        print('-------------------------------------------')
        print('Cajero: ',usuario[0][0],'      Fecha: ',venta[0][4])
        print('-------------------------------------------')
        print('Cliente: ',cliente[0][0])
        print('-------------------------------------------')
        print('--------------DETALLES---------------------')
        print('-------------------------------------------')
        print("Nro\tproducto\tcantidad\tsubtotal")
        i = 0
        for detalle in detalles:
            producto = db.select("producto","nombre",f"id_producto = {detalle[1]}")
            print(f"{i}\t{producto[0][0]}\t{detalle[1]}\t{detalle[2]}\t{detalle[3]}")
            i += 1 
        print('-------------------------------------------')
        print('Total a pagar: $', venta[0][5])
        print('-------------------------------------------')
        print("")
        
        db.close()