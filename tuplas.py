primeraTupla=("Fabricio Vargas Alvarez", 1999,"Emi", False, "Emi", "Emi")# se crea con paréntesis no con corchetes
#también las tuplas se pueden hacer sin parentésis

nombre,ano,diminutivo1,boolean,diminutivo2,diminutivo3=primeraTupla #asigno los valores a las variables

listaTupla=list(primeraTupla) #creo una lista a partir de la tupla que ya cree

listaMes=["Enero","Febrero","Marzo","Abril","Mayo"]
tuplaLista=tuple(listaMes)

print(primeraTupla[2])#imprime la tubla en la posición 2
print(1999 in primeraTupla)
print(primeraTupla.count("Emi"))
print(len(primeraTupla))#Cantidad de elementos en la tupla

print(listaTupla)#imprimo la lista de la tupla

print(tuplaLista)

mitupla=("Fabricio",) #Esto es una tupla unitaria

# Las tublas si se pueden buscar por medio del index, esto es una correción
