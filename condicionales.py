print("Programa de evaluacion de notas de alumnos")

notas=input("Introduce la nota del alumno: ")#El input siempre da por defecto un valor de estring

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Reprovado"
    return(valoracion)

print(evaluacion(int(notas)))# Uso la variable int para que no de problemas en el if



print("Entrega de notas finales")

nota=int(input("Ingrese su nota final: "))
def validacionNotas(nota):
    if nota<5:
        print("Insuficiente")
    elif nota<5: #Si uno no pone un elif entonces el else solo cubre al segundo if y al primero no
        print("Suficiente")
    elif nota<7: #Si uno no pone un elif entonces el else solo cubre al segundo if y al primero no
        print("Bien")
    elif nota<9: #Si uno no pone un elif entonces el else solo cubre al segundo if y al primero no
        print("Notable")
    else:
        print("Sobresaliente")

validacionNotas(nota)
