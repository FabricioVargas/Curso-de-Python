#Aplica una función a cada elemento de una lista iterable, devuelve una lista
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):# Devolver informacion del objeto
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleado=[

Empleado("Fabricio","Director",75000),
Empleado("Vannesa","Jefa",85000),
Empleado("Emi","Manager",25000),
Empleado("Ale","Administradora",27000),
Empleado("Norito","Dueña",21000),

]

def calculoComision(empledo):
    empledo.salario=empledo.salario*1.03
    return empledo

listaEmpleadosComision=map(calculoComision,listaEmpleado)#se le agrega la funcion y luego la lista

for i in listaEmpleadosComision:
    print(i)
