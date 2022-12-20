from Database import sql
class Cliente:

    def __init__(self,id_cliente = 0, nombre = "", apellido="", direccion="", telefono="", fecha_nacimiento="", dni="", email="", condicion_fiscal="",estado=1):
        self.__idcliente = id_cliente
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__dni = dni
        self.__email = email
        self.__condicion_fiscal = condicion_fiscal
        self.__estado = estado

    @property
    def Idcliente(self):
        return self.__idcliente
    
    @Idcliente.setter
    def Idcliente(self, idcliente):
        self.__idcliente = idcliente
    
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def Apellido(self):
        return self.__apellido
    
    @Apellido.setter
    def Apellido(self, apellido):
        self.__apellido = apellido

    @property
    def Direccion(self):
        return self.__direccion
    
    @Direccion.setter
    def Direccion(self, direccion):
        self.__direccion = direccion
    
    @property
    def Telefono(self):
        return self.__telefono
    
    @Telefono.setter
    def Telefono(self, telefono):
        self.__telefono = telefono
    
    @property
    def Fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @Fecha_nacimiento.setter
    def Fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    
    @property
    def Dni(self):
        return self.__dni
    
    @Dni.setter
    def Dni(self, dni):
        self.__dni = dni
    
    def __str__(self):
        return self.__nombre + " " + self.__apellido + " - " + self.__direccion + " - " + self.__telefono          
    
    @property
    def Email(self):
        return self.__email
    
    @Email.setter
    def Email(self, email):
        self.__email = email
    
    @property
    def condicion_fiscal(self):
        return self.__condicion_fiscal
    
    @condicion_fiscal.setter
    def condicion_fiscal(self, condicion_fiscal):
        self.__condicion_fiscal = condicion_fiscal
    
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self, estado):
        self.__estado = estado
    
    def __str__(self):
        return super().__str__() + " - " + self.__email + " - " + self.__condicion_fiscal + " - " + self.__estado
    
    def crearCliente(self):
        self.Nombre    = input("Ingrese el nombre del cliente: ")
        self.Apellido  = input("Ingrese el apellido del cliente: ")
        self.Direccion = input("Ingrese la direccion del cliente: ")
        self.Telefono  = input("Ingrese el telefono del cliente: ")
        self.Fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente: ")
        self.Dni = input("Ingrese el dni del cliente: ")
        self.__email = input("Ingrese el email del cliente: ")
        self.__condicion_fiscal = input("Ingrese condicion fiscal: ")
        db = sql.DataBase('superpy.db')
        db.insert("cliente","nombre,apellido,dni,direccion,telefono,fecha_nacimiento,email,condicion_fiscal",
                  f"'{self.Nombre}','{self.Apellido}','{self.Dni}',"+
                  f"'{self.Direccion}','{self.Telefono}','{self.Fecha_nacimiento}',"+
                  f"'{self.__email}','{self.__condicion_fiscal}'"
                  )
        db.close()
        
    def modificarCliente(self,id_cliente):
        db = sql.DataBase('superpy.db')
        cliente = db.select("cliente","nombre,apellido,dni,direccion,telefono,fecha_nacimiento,email,condicion_fiscal,estado",
                  f"id_cliente = {id_cliente}")
        print("Si no desea Modificar el Dato Solo Presione Enter")
        print("Hasta llegar al Dato que quiere modificar")
        self.Nombre    = input(f"Modifica el Nombre {cliente[0][0]} : ") or cliente[0][0]
        self.Apellido  = input(f"Modifica el Apellido {cliente[0][1]} : ") or cliente[0][1]
        self.Dni = input(f"Modifica el DNI : {cliente[0][2]}") or cliente[0][2]
        self.Direccion = input(f"Modifica la Direccion {cliente[0][3]}: ") or cliente[0][3]
        self.Telefono  = input(f"Modifica el telefono {cliente[0][4]}: ")
        self.Fecha_nacimiento = input(f"Modifica la fecha de nacimiento {cliente[0][5]} :") or cliente[0][5]
        self.__email = input(f"Modifica email {cliente[0][6]}: ") or cliente[0][6]
        self.__condicion_fiscal = input(f"Modifica condicion fiscal {cliente[0][7]} :") or cliente[0][7]
        self.__estado = input(f"Modifica el estado {cliente[0][8]} :") or cliente[0][8]
        db.update("cliente","nombre",f"'{self.Nombre}'",f"id_cliente = {id_cliente}")
        db.update("cliente","apellido",f"'{self.Apellido}'",f"id_cliente = {id_cliente}")
        db.update("cliente","dni",f"'{self.Dni}'",f"id_cliente = {id_cliente}")
        db.update("cliente","direccion",f"'{self.Direccion}'",f"id_cliente = {id_cliente}")
        db.update("cliente","telefono",f"'{self.Telefono}'",f"id_cliente = {id_cliente}")
        db.update("cliente","fecha_nacimiento",f"'{self.Fecha_nacimiento}'",f"id_cliente = {id_cliente}")
        db.update("cliente","email",f"'{self.__email}'",f"id_cliente = {id_cliente}")
        db.update("cliente","condicion_fiscal",f"'{self.__condicion_fiscal }'",f"id_cliente = {id_cliente}")
        db.update("cliente","estado",f"'{self.__estado }'",f"id_cliente = {id_cliente}")
        db.close()
    
    def eliminarCliente(self,id_cliente):
        self.__estado = 0
        db = sql.DataBase("superpy.db")
        db.update("cliente","estado",f"'{self.__estado}'",f"id_cliente = {id_cliente}")
        db.close()
    
    def listarClientes(self):
        db = sql.DataBase("superpy.db")
        clientes = db.select_all("cliente","id_cliente,nombre,apellido,dni,direccion,telefono,fecha_nacimiento,email,condicion_fiscal,estado")
        print("------------------------------------------------------------------------------------------------------")
        print("Nro\tnombre\tapellido\tdni\tdireccion\ttelefono\tfecha_nacimiento\temail\t\t\tcondicion_fiscal\testado")
        for cliente in clientes:
            if {cliente[9]} != 0:
                print(f"{cliente[0]}\t{cliente[1]}\t{cliente[2]}\t{cliente[3]}\t{cliente[4]}\t\t{cliente[5]}\t{cliente[6]}\t{cliente[7]}\t{cliente[8]}\t{cliente[9]}")
        print("------------------------------------------------------------------------------------------------------")
        db.close()       
        

