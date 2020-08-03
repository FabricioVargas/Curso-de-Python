from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()
operacion=""#Variable global
resultado=0#va a almacenar la suma de los valores introducidos

#-----------------------------Pantalla--------------------------------

numeroPantalla=StringVar(value="0")#Creo una variable donde van a ir los numeros
pantalla=Entry(miFrame,textvariable=numeroPantalla)#Asigno los numeros a la pantalla
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4) #columnspan=4 le digo a la pantalla que tome un tamaño de cuatro columnas
pantalla.config(background="black",fg="#03f943",justify="right")

#--------------------------Pulsaciones teclado----------------------------------
def numeroPresionado(num):
    global operacion
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    elif numeroPantalla.get()=="0" and num=="0":
        numeroPantalla.set("0")
    else:
        numeroPantalla.set(numeroPantalla.get()+ num)

#----------------------------funcion suma------------------------------------------
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeroPantalla.set(resultado)

#----------------------------funcion el_resultado------------------------------------------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0

#-------------------------Fila1---------------------------------------------
boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPresionado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPresionado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPresionado("9"))
boton9.grid(row=2, column=3)
botonDividir=Button(miFrame,text="/",width=3)
botonDividir.grid(row=2, column=4)

#---------------------------------Fila2----------------------------------------

boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPresionado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPresionado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPresionado("6"))
boton6.grid(row=3, column=3)
botonMultiplicar=Button(miFrame,text="X",width=3)
botonMultiplicar.grid(row=3, column=4)

#---------------------------------Fila3----------------------------------------

boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPresionado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPresionado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPresionado("3"))
boton3.grid(row=4, column=3)
botonRestar=Button(miFrame,text="-",width=3)
botonRestar.grid(row=4, column=4)

#---------------------------------Fila4----------------------------------------

botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPresionado(","))
botonComa.grid(row=5, column=1)
boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPresionado("0"))
boton0.grid(row=5, column=2)
botonSuma=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=3)
botonIgual=Button(miFrame,text="=",width=3,command=lambda: el_resultado())
botonIgual.grid(row=5, column=4)

miFrame.mainloop()
