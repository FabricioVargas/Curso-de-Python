from tkinter import *

# Se crea la primer ventana
raiz=Tk()

#Modificar la ventana por defecto
raiz.title("Ventana de pruebas")
#raiz.resizable(False,False)#width y height para que no se redimencionar
# raiz.iconbitmap("imagen") Esto me permite agregar el icono a la ventana
raiz.geometry("550x350")#Tamaño de la Ventana
raiz.config(bg="blue")

miFrame=Frame()#Creo el frame
#miFrame.pack(side="lefth",anchor="n")#Lo empaqueto: buttom, anchor son los puntos cardinales
miFrame.pack(fill="both",expand=True)# si no lo tengo redimencionado,cuando crezca la raiz, también crece el frame
miFrame.config(bg="red")#color de fondo
miFrame.config(width="650",height="350")#tamaño del frame
miFrame.config(relief="groove") #hace un borde con miframe.config(bd=35)


raiz.mainloop()#El mainloop simpre tiene que ir de último
