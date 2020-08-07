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

salario_alto=filter(lambda empleado:empleado.salario>21000,listaEmpleado)

for i in salario_alto:
    print(salario_alto)
