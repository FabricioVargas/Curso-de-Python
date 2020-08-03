 from tkinter import *
root=Tk()

miFrame=Frame(root,width="500",height="400")
miFrame.pack()

miLabel = Label(miFrame,text="Hola alumnos de Python")
#miLabel.pack() si se empaqueta el label va a destruir el width y height que le pusimos al inicio
miLabel.place(x=100, y=200)# Pone el texto en un punto en concreto

#miImagen=PhotoImage(file="ruta de la imagen")
#Label(miFrame,Image=miImagen).place(x=100, y=200) le asigno a un label la imagen


Label(miFrame,text="Hola alumnos de Python",fg="red",font=("Comic Sans MS",18)).place(x=100, y=200)# otra forma de hacer labels abrevidados
root.mainloop()
