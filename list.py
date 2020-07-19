mesesList=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto']#Hacerlo con comillas simple

print(mesesList[3])#si se le pone un número negativo comienza de atras hacia adelante

print(mesesList[2:6])#devualve esa porción de la lista, incluye el 2, excluye el 6

print(mesesList[2:])#imprime todos despúes del indice 2, incluyendo el 2

mesesList.append('Septiembre')#Agrego a una lista al final
mesesList.insert(2,"Pedro")# Se agrega la posición donde va a ir y el elemento
mesesList.extend(["Octubre","Noviembre","Diciembre"])#Agrega varios elementos al final
mesesList.remove("Enero")#Elimina un elemento de la lista

print(mesesList)

print(mesesList.index("Febrero"))# Posicion de un elemento en una lista

print("Mayo" in mesesList) #Me dice con un boolean si el elemento esta en la lista

randonList=['Enero',23,'Marzo',True,'Mayo',36.99]

randonList.remove(23)
randonList.pop() #Elimina el último elemento de la lista

print(randonList)
print(randonList[3])

listaUno=[1,2,3,4,5]
listaDos=[6,7,8,9,10]

listaTres=listaUno+listaDos
print(listaTres)
