from tkinter import *
root=Tk()
root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opcionViaje():
    opcionesEscogida=""
    if playa.get()==1:
        opcionesEscogida+=" playa"
    if montana.get()==1:
        opcionesEscogida+=" montana"
    if turismoRural.get()==1:
        opcionesEscogida+=" turismoRural"
    textFinal.config(text=opcionesEscogida)
Checkbutton(root,text="Playa",variable=playa, onvalue=1,offvalue=0,command=opcionViaje).pack() #onvalue para decirle que esta seleccionado, cuando se quita la seleccion
# queda como onvalue
Checkbutton(root,text="Montaña",variable=montana, onvalue=1,offvalue=0,command=opcionViaje).pack()
Checkbutton(root,text="Turismo rural",variable=turismoRural, onvalue=1,offvalue=0,command=opcionViaje).pack()

textFinal=Label(root)
textFinal.pack()

root.mainloop()
