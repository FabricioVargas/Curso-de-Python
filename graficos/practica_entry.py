from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

miNomnbre=StringVar()#Cadena de caracteres

cuadroNombre=Entry(miFrame, textvariable=miNomnbre) #  textvariable=miNomnbre asignamos esa variable para que aparezca escrito
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)#lleva el row y column
cuadroNombre.config(fg="red")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1, padx=10, pady=10)#lleva el row y column

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1, padx=10, pady=10)#lleva el row y column

cuadroContrasenia=Entry(miFrame)
cuadroContrasenia.grid(row=3,column=1, padx=10, pady=10)#lleva el row y column
cuadroContrasenia.config(show="*")

cuadroComentario=Text(miFrame, width=16,height=5)#Creo un texto
cuadroComentario.grid(row=4,column=1, padx=10, pady=10)#lleva el row y column
scroll=Scrollbar(miFrame,command=cuadroComentario.yview)# cuadroComentario: donde pertenece .yview: que sea de forma vertical
scroll.grid(row=4,column=2, sticky="nsew")# sticky="nsew": tamaño del largo del scroll
cuadroComentario.config(yscrollcommand=scroll.set)
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e", padx=10, pady=10)# sticky(puntos cardinales) permite colocar el contenido de los label donde uno quiera

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0, padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2,column=0, padx=10, pady=10)

contraseniaLabel=Label(miFrame, text="Contraseña: ")
contraseniaLabel.grid(row=3,column=0, padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4,column=0, padx=10, pady=10)

def codigoBoton():
    miNomnbre.set("Fabricio")

botonEnviar=Button(raiz,text="Enviar",command=codigoBoton)
botonEnviar.pack()

raiz.mainloop()
