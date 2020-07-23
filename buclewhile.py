import math
i=1

while i<5:
    print("hola " + str(i))
    i=i+1

edad=int(input("Edad: "))

while edad<0:
    print("La edad no puede ser negativa")
    edad=int(input("Vuelve a introducir la edad: "))
print("edad aceptada")

print ("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0
while numero<0:
    print("No se puede hallar la raiz de un número negativo")
    numero=int(input("Vuelva a introduce un numero: "))
    intentos=intentos+1

    if intentos==2:
        print("Has consumido demasiados intentos. EL programa va a finalizar")
        break;
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " +str(numero)+ " es: " + str(solucion))
