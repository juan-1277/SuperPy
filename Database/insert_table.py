import sql

db = sql.DataBase("superpy.db")

db.insert("rol","nombre,descripcion","'Administrador','Administrador del sistema'")

db.insert("usuario","nombre,apellido,dni,email,password,idrol","'Llatser','Juan','12345678','juanllatser@gmail.com','1277',1")


db.close()