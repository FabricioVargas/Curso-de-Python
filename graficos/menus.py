from tkinter import *
from tkinter import messagebox #Libreria para importar los mensajes

root = Tk()

#Funcion que construlle el mensaje emergente
def infoAdicional():
    messagebox.showinfo("Procesador de Fabricio","Procesador de textos 2020")# texto de arriba como primer parametro, luego texto en el centro como segundo parametro

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salir():
    valor=messagebox.askquestion("Guradar", "Desea guardar este archivo")# Acepta, cancelar: devuelve yes o not
    #valor=messagebox.askokcancel("Guradar", "Desea guardar este archivo")#el valor que devuelve es True o False
    if valor=="yes":
        root.destroy()

def reintentar():
    messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento cerrado")
    if valor=="yes":
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)
archivoMenu=Menu(barraMenu,tearoff=0)#tearoff=0 quita una barra que se hace en el inicio

#Agregamos items al apartado de ARCHIVO
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Gurdar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()#hace una line separadora entre los items
archivoMenu.add_command(label="Cerrar",command=lambda:reintentar())
archivoMenu.add_command(label="Salir",command=lambda:salir())

archivoEdicion=Menu(barraMenu,tearoff=0)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)

archivoAyuda.add_command(label="Licencia",command=lambda:avisoLicencia())
archivoAyuda.add_command(label="Acerca de",command=lambda:infoAdicional())

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)#cuado hago el proceso de agregado debo darle el texto a cada una de las partes que no lo trae
barraMenu.add_cascade(label="Edición",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


root.mainloop()
