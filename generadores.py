def generarPares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1
devuelvePares=generarPares(10)

print(next(devuelvePares))# imprime 2 si lo vuelvo a llamar llama al 4 y así va

for i in devuelvePares:
    print(i)


def devuelveCiudades(*ciudades):# el asterizco nos dice que no sabe cuantos elementos va a recibir y los recibe en una tupla
    for elemento in ciudades:
        #for subElemento in elemento: #accedo al primer elemento pero con esto accedo a la primer letra del elemento
            yield from elemento

ciudades_devueltas= devuelveCiudades("Grecia","Sarchi","Narajo","Palmares")

print(next(ciudades_devueltas))
