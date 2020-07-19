salarioPresidente=int(input("Ingrese el salario del Presidente de la empresa: "))
salarioDirector=int(input("Ingrese el salario del directir de la empresa: "))
salarioJefeAministrativo=int(input("Ingrese el salario del jefe administrativo de la empresa: "))
salarioAministrativo=int(input("Ingrese el salario del administrativo de la empresa: "))

print("El salario del jefe es :" + str(salarioPresidente))

if salarioAministrativo<salarioJefeAministrativo<salarioDirector<salarioPresidente:
    print("Los salarios fueron ingresados correcatmente")
else:
    print("Hay diferencia entre los salarios")

#funcion str() me permite convertir un int a estring para concatenarlo a un texto

print("Asignaturas optativas")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Introduce la asignatura escogida: ")

asignatura=opcion.lower()
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura eligida " + asignatura)
else:
    print("Asignatura no contemplada")
