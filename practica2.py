def numerosImpares():
    for i in range(1,100,2):
        print(i, end=" ")

#numerosImpares()

def reconociendoContrasena():
    contador=0
    contrasena=input("Por favor escriba su contraseña: ")
    for i in range(len(contrasena)):
        if contrasena[i]==" ":
            continue

        else:
            contador+=1

    if contador>=8:
        return print("Contraseña Ok")
    else:
        return print("Contraseña Erronea")

#reconociendoContrasena()

def evaluacionCorreo():
    a=0
    p=0
    correo=input("Por favor ingrese su contraseña: ")
    for i in correo:
        if i=="@":
            a+=1
        if i==".":
            p+=1
    if a==1 and p>=1:
        return print("Correo correcto")
    else:
        return print("Correo incorrecto")

evaluacionCorreo()
