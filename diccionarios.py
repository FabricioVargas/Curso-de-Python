#el primer dato es la clave, el segundo es el valor
primerDiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Espana":"Madrid"}
segundoDiccionario={"Alemania":"Berlin",21:"Fabricio","Mosqueteros":123}
primerDiccionario["Italia"]="Roma"#Agrega un nuevo elemento al diccionario
del primerDiccionario["Espana"]# Elimino un elemento del diccionario

print(primerDiccionario)
print(primerDiccionario["Alemania"])# Aquí pongo la clave del valor que quiero buscar


tupla= ("Espana","Francia","Reino Unido","Alemania")
midiccionario={tupla[0]:"Madrid",tupla[1]:"Paris",tupla[2]:"Londres",tupla[3]:"Berlin"}
print(midiccionario)

diccionario={23:"Jordan","Nombre":"Fabricio","Equipo":"Saprissa","anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())#Devuelve todas las llaves primarias
print(midiccionario.values())#Devuelve los valores que tienen las claves
print(len(midiccionario))#Devuelve la cantidad de valores del diccionario
print(diccionario["anillos"])

print(diccionario["anillos"]["Temporadas"][2])
