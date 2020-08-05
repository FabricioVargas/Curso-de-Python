from Model import *

def conexionBD():
    return conexionBBDD()

#def crearUsuario(varId,varNombre,varContrasenia,varApellido,varDireccion,cuadroComentario):
    #return  crear(varId,varNombre,varContrasenia,varApellido,varDireccion,cuadroComentario)

def cargarUsuario(varId):
    return leer(varId)
