import sqlite3

miConexion= sqlite3.connect("PrimeraBase")#Abrir-Crear

miCursor=miConexion.cursor()#Creo el cursor

#miCursor.execute("CREATE TABLE producto (nombreArticulo varchar(50), precio integer,seccion varchar(20))")
#miCursor.execute("INSERT INTO producto values('Balon',15,'Deportes')")

#variosProsuctos=[
    #("Camiseta",10,"Deportes"),
    #("Jarrón",90,"Cerámica"),
    #("Camión",20,"Juguetería")
#]
#miCursor.executemany("INSERT INTO producto values(?,?,?)",variosProsuctos)#Inserta un lote de registros en la tabla


miCursor.execute("select * from producto")

variosProsuctos=miCursor.fetchall()#Devuelve una listo de productos y los guardo en una variable

print(variosProsuctos)

miConexion.commit()

miConexion.close()#Cerrar base de datos
