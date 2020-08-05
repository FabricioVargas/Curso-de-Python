from tkinter import *
from tkinter import messagebox
from Controller import *
import sqlite3

global root

root=Tk()#Se crea la Ventana


root.title("CRUD")
root.geometry("400x400")

#----------------Creo los frames----------------------

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

btnFrame=Frame(root,width=1200,height=100)
btnFrame.pack()

#------------------Variables---------------------------
varId=StringVar()
varNombre=StringVar()
varContrasenia=StringVar()
varApellido=StringVar()
varDireccion=StringVar()

#-------------------------creacion de los labels y entrys

#--------------ID
idLabel=Label(miFrame, text="ID: ")
idLabel.grid(row=2,column=0,padx=10,pady=10,sticky="w")

cuadroID=Entry(miFrame,textvariable=varId)
cuadroID.grid(row=2,column=1,padx=10,pady=10,sticky="w")

#--------------Nombre
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=3,column=0,padx=10,pady=10,sticky="w")

cuadroNombre=Entry(miFrame,textvariable=varNombre)
cuadroNombre.grid(row=3,column=1,padx=10,pady=10,sticky="w")

#--------------Contraseña
contrasenaLabel=Label(miFrame, text="Contraseña: ")
contrasenaLabel.grid(row=4,column=0,padx=10,pady=10,sticky="w")

cuadroContrasenia=Entry(miFrame,textvariable=varContrasenia)
cuadroContrasenia.grid(row=4,column=1,padx=10,pady=10,sticky="w")
cuadroContrasenia.config(show="*")

#--------------Apellido
apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=5,column=0,padx=10,pady=10,sticky="w")

cuadroApellido=Entry(miFrame,textvariable=varApellido)
cuadroApellido.grid(row=5,column=1,padx=10,pady=10,sticky="w")

#--------------Direccion
direccionLabel=Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=6,column=0,padx=10,pady=10,sticky="w")

cuadroDireccion=Entry(miFrame,textvariable=varDireccion)
cuadroDireccion.grid(row=6,column=1,padx=10,pady=10,sticky="w")

#---------------Comentario
comentarioLabel=Label(miFrame, text="Cometarios: ")
comentarioLabel.grid(row=7,column=0,padx=10, pady=10,sticky="w")

cuadroComentario=Text(miFrame, width=16,height=5)#Creo un texto
cuadroComentario.grid(row=7,column=1, padx=10, pady=10,sticky="w")#lleva el row y column
scroll=Scrollbar(miFrame,command=cuadroComentario.yview)# cuadroComentario: donde pertenece .yview: que sea de forma vertical
scroll.grid(row=7,column=2, sticky="nsew")# sticky="nsew": tamaño del largo del scroll
cuadroComentario.config(yscrollcommand=scroll.set)

#---------------------Botones
btnCreate=Button (btnFrame,text="Create",command=lambda:crear())
btnCreate.grid(row=9, column=0,padx=10, pady=10)

btnRead=Button (btnFrame,text="Read",command=lambda:llenarCampos())
btnRead.grid(row=9, column=1,padx=10, pady=10)

btnUpdate=Button (btnFrame,text="Update",command=lambda:modificar())
btnUpdate.grid(row=9, column=2,padx=10, pady=10)

btnDelete=Button (btnFrame,text="Delete",command=lambda:eliminar())
btnDelete.grid(row=9, column=3,padx=10, pady=10)

#--------------Menu
barraMenu=Menu(root)
root.config(menu=barraMenu,width=1200,height=50)


bbdd=Menu(barraMenu,tearoff=0)
bbdd.add_command(label="Conectar",command=lambda:conexionBD())
bbdd.add_command(label="Salir", command=lambda:salirAplicacion())

borrar=Menu(barraMenu,tearoff=0)
borrar.add_command(label="Borrar campos",command=lambda:limpiarCampos())

crud=Menu(barraMenu,tearoff=0)
crud.add_command(label="Create",command=lambda:crear())
crud.add_command(label="Read",command=lambda:llenarCampos())
crud.add_command(label="Update",command=lambda:modificar())
crud.add_command(label="Delete",command=lambda:eliminar())

ayuda=Menu(barraMenu,tearoff=0)
ayuda.add_command(label="Licencia")
ayuda.add_command(label="Acerca de")


#---------------------Creo los titulos
barraMenu.add_cascade(label="BBDD",menu=bbdd)
barraMenu.add_cascade(label="Borrar",menu=borrar)
barraMenu.add_cascade(label="CRUD",menu=crud)
barraMenu.add_cascade(label="Ayuda",menu=ayuda)

#-------------Funcion salir------------------------
def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def limpiarCampos():
    varId.set("")
    varNombre.set("")
    varContrasenia.set("")
    varApellido.set("")
    varDireccion.set("")
    cuadroComentario.delete(1.0,END)# le decimos que borre desde el inicio con 1.0 hasta el final (end)

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
    limpiarCampos()

def llenarCampos():
    conexion=sqlite3.connect("Usuarios")
    cursor=conexion.cursor()
    cursor.execute('''SELECT * FROM datosUsuario WHERE id=?''',(varId.get()))
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

def modificar():
    valor = messagebox.askquestion("Actualizar Registro","¿Desea actualizar el registro?")
    if valor == "yes":
        conexion = sqlite3.connect("Usuarios")
        cursor=conexion.cursor()

        info=varNombre.get(),varContrasenia.get(),varApellido.get(),varDireccion.get(),cuadroComentario.get("1.0",END),varId.get()
        cursor.execute('''UPDATE datosUsuario
        SET nombre=?,contrasenia=?,apellido=?,direccion=?,comentarios=?
        WHERE id=?''',(info))
        conexion.commit()
        conexion.close()

    messagebox.showinfo("BBDD","Registro actualizado con exito")
    limpiarCampos()

def eliminar():
    valor = messagebox.askquestion("Eliminar Registro","¿Desea eliminar registro?")
    if valor == "yes":
        conexion=sqlite3.connect("Usuarios")
        cursor= conexion.cursor()
        cursor.execute("DELETE FROM datosUsuario WHERE id=?",(varId.get()))
        conexion.commit()
        conexion.close()

    messagebox.showinfo("BBDD","Registro borrado con éxito")
    limpiarCampos()

root.mainloop()
