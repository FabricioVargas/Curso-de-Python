import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()# Se utiliza para controlar las sentencias sql

miCursor.execute('''
    CREATE TABLE productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_aerticulo varchar(50) UNIQUE,
    precio integer,
    seccion varchar(20)
    )
''') #Cuando la sentencia se quiere dividir en varios reglones utilizo la triple comilla
# id INTEGER PRIMARY KEY AUTOINCREMENT: campo autoincremental y al mismo tiempo llave primaria

listaProductos=[#No pongo el campo de id porque es autoincremental
    ("pelota",20,"juguetería"),
    ("pantalón",20,"confección"),
    ("desatornillador",20,"ferretería"),
    ("jarrón",20,"cerámica")
]

miCursor.executemany("INSERT INTO productos values (NULL,?,?,?)",listaProductos)#Pongo null en el campo autoincremental

miCursor.execute("SELECT * FROM productos")
resultado=miCursor.fetchall()
print(resultado)

#Read
miCursor.execute("SELECT * FROM productos WHERE seccion='juguetería'")
leer=miCursor.fetchall()
print(leer)

#Update
miCursor.execute("UPDATE productos set precio=20 WHERE nombre_aerticulo='pelota'")

#Delete
miCursor.execute("DELETE FROM productos WHERE id=5")

miConexion.commit()
miConexion.close()
