from tkinter import *
from tkinter import filedialog# clase que importo para cargar archivos

root = Tk()

def abrirFicher():
    fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:/",filetypes=(("Ficheros de word","*.doc"),
    ("Ficheros de texto","*.txt")))#initialdir="" directorio donde quiero iniciar a buscar, no es necesario
    print(fichero)# devuelve la ruta del archivo

Button (root,text="Abrir Fichero", command=abrirFicher).pack()

root.mainloop()
