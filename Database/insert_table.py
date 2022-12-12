import sql

db = sql.DataBase("superpy.db")

db.insert("rol","nombre,descripcion","'Administrador','Administrador del sistema'")

db.insert("usuario","nombre,apellido,dni,email,password,idrol","'Llatser','Juan','12345678','juanllatser@gmail.com','1277',1")

db.insert("usuario","nombre,apellido,dni,email,password,idrol","'Camaño','Maxi','99999','maxicamano@gmail.com','3333',1")
#para agregar un usuario nuevo simplemente agrego un db.insert("nombre de tabla", "las columnas de las tablas a insertar", datos de cada columna)



db.close()