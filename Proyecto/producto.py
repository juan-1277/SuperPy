from Database import sql

class Producto:
    def __init__(self,id_producto = 0,id_categoria = 0,codigo="",nombre="",precio_venta = 0,stock = 0,descripcion = "",estado = 1):
        self.__id_producto = id_producto
        self.__id_categoria = id_categoria
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_venta = precio_venta
        self.__stock = stock
        self._descripcion = descripcion
        self.__estado = estado
    
    #getter y setter
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self,estado):
        self.__estado = estado
    
    def create_producto(self):
        db = sql.DataBase("superpy.db")
        db.insert("producto","codigo,nombre,precio_venta,stock,descripcion",
                f"'{self.__codigo}','{self.__nombre}','{self.__precio_venta}','{self.__stock}','{self.__descripcion}'")
    
    def get_all_producto(self):
        db = sql.DataBase("superpy.db")
        producto = db.select_all("producto","codigo,nombre,precio_venta,stock,descripcion")
        return producto

    def update_producto(self,id,datos):
        db = sql.DataBase("superpy.db")
        for k,v in datos:
            db.update("producto",k,v,f"id_producto = {id}")
    
    def delete_producto(self,id):
        db = sql.DataBase("superpy.db")
        db.update("producto","estado",0,f"id_producto = {id}")