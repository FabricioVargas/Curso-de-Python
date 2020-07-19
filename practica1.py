import statistics
print("DevuelveMax")

numeroUno=int(input("Escriba el primer número: "))
numeroDos=int(input("Escriba el segundo número: "))

def devuelveMax(numeroUno,numeroDos):
    if numeroUno<numeroDos:
        print(numeroDos)
    elif numeroDos<numeroUno:
        print(numeroUno)
    else:
        print("Los numero son iguales")

devuelveMax(numeroUno,numeroDos)

#----------------------------------------------------------------------
informacion=[]
nombre=input("Digite su nombre: ")
direccion=input("Digite su dirección: ")
telefono=input("Digite su numero telefonico: ")

informacion.extend([nombre,direccion,telefono])

print("Los datos personales son: " + informacion[0]+ " " +informacion[1]+" "+informacion[2])

#-------------------------------------------------------------------------
numeroUno=int(input("Escriba el primer número: "))
numeroDos=int(input("Escriba el segundo número: "))
numeroTres=int(input("Escriba el segundo número: "))

media=(numeroUno+numeroDos+numeroTres)/3

print(media)

list=[numeroUno,numeroDos,numeroTres]
print(statistics.mean(list))
