def incrementandoNumeros():
    numero=int(input("Selecione un número por favor: "))
    numero2=int(input("Selecione un número mayor por favor: "))
    while numero2 > numero:
        numero=numero2
        numero2=int(input("Selecione un número mayor por favor: "))
    print("Ha ingresado un numero menor o igual a " + str(numero))
#incrementandoNumeros()

def incrementandoNumerosPositivos():
    numero=int(input("Selecione un número positivo por favor: "))
    suma=0
    while numero>0:
        suma=suma+numero
        numero=int(input("Selecione ptro numero positivo por favor: "))
    print("Se ha ingresado un numero negativo. Suma total:  " + str(suma))

#incrementandoNumerosPositivos()

def validanEmail():
    correo=input("Por favor ingrese su correo electrónico: ")
    contador=correo.count("@")
    print(contador)
    if (contador!=1 or correo.rfind("@")==(len(correo)-1) or correo.find("@")==0) :
        print("Correo incorrecto")
    else:
        print("Correo correcto")

validanEmail()
