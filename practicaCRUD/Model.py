import sqlite3
from tkinter import messagebox

def conexionBBDD():
    conexion = sqlite3.connect("Usuarios")
    cursor=conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE datosUsuario (id varchar(50) primary key,
            nombre varchar(50),
            contrasenia varchar(15),
            apellido varchar(50),
            direccion varchar(50),
            comentarios varchar(60))''')
        messagebox.showinfo("BBDD","BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!","La BBDD ya existe")
    conexion.close()

def crear():
    conexion = sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    #crearUsuario(varId,varNombre,varContrasenia,varApellido,varDireccion,cuadroComentario)
    #cursor.execute("INSERT INTO datosUsuario VALUES('"+ varId.get()+ "','" +varNombre.get()+ "','"+varContrasenia.get()+"','"+varApellido.get()+"','"+varDireccion.get()+"','"+cuadroComentario.get("1.0",END)+"')")
    #La sentencia de arriba funciona pero puede tener afrontar inyeccion sql
    info=varId.get(),varNombre.get(),varContrasenia.get(),varApellido.get(),varDireccion.get(),cuadroComentario.get(1.0,END)
    cursor.execute("INSERT INTO datosUsuario (id,nombre,contrasenia,apellido,direccion,comentarios) VALUES (?,?,?,?,?,?)",(info))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("BBDD","Registro insertado con exito")

def leer(varId):
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM datosUsuario WHERE id=" + varId.get())
    usuario=cursor.fetchall()

    for i in usuario:
        varId.set(i[0])
        varNombre.set(i[1])
        varContrasenia.set(i[2])
        varApellido.set(i[3])
        varDireccion.set(i[4])
        cuadroComentario.insert(1.0,i[5])

    conexion.commit()
    conexion.close()
