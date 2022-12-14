import sql

db = sql.DataBase("superpy.db")

db.create_table("rol","id_rol INTEGER PRIMARY KEY AUTOINCREMENT," +  
                       "nombre TEXT," + 
                       "descripcion TEXT," + 
                       "estado INTEGER DEFAULT 1"
                )

db.create_table("usuario","id_usuario INTEGER PRIMARY KEY AUTOINCREMENT," +
                          "nombre TEXT," +
                          "apellido TEXT," +
                          "dni TEXT," +
                          "email TEXT,"  +
                          "password TEXT," + 
                          "id_rol INTEGER," +
                          "estado INTEGER DEFAULT 1" 
                )

db.create_table("cliente","id_cliente INTEGER PRIMARY KEY AUTOINCREMENT," +
                        "nombre TEXT(50)," +
                        "apellido TEXT(50)," +
                        "dni TEXT(11)," + 
                        "direccion TEXT(100)," +
                        "fecha_nacimiento datetime," +
                        "telefono TEXT(15)," +
                        "email TEXT(100)," +
                        "condicion_fiscal TEXT(100),"+
                        "estado INTEGER DEFAULT 1"
                )

db.create_table("venta",
                "id_venta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "id_cliente INTEGER,"+
                "tipo_comprobante TEXT(20),"+
                "nro_comprobante TEXT(7),"+
                "fecha TEXT(10),"+
                "total REAL,"+
                "estado INTEGER DEFAULT 1,"+
                "id_usuario INTEGER"
                )

db.create_table("detalle_venta", 
                "id_detalle_venta INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "id_venta INTEGER,"+
                "id_producto INTEGER,"+
                "cantidad INTEGER,"+
                "precio REAL"
                )

db.create_table("producto",
                "id_producto INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "id_categoria INTEGER,"+
                "codigo TEXT(20)," +
                "nombre TEXT(70),"+
                "precio_venta REAL,"+
                "stock INTEGER,"+
                "descripcion TEXT(256),"+
                "estado INTEGER DEFAULT 1"
                )

db.create_table("categoria",
                "id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "nombre TEXT(100),"+
                "descripcion TEXT(256),"+
                "estado INTEGER DEFAULT 1"
                )

db.close()
