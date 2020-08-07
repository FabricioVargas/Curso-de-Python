import re
#Metacaracteres
#Vamos a ver ejemplos de anclas video 71

#Con las anclas vamos ha encontrar similitudes de texto al inicio y al final
listaNombres=['http://pildorasinformaticas.es',
              'ftp://pildorasinformaticas.es',
              'http://pildorasinformaticas.com',
              'ftp://pildorasinformaticas.com']

listaCosas=['hombre',
            'camión',
            'camion']

listaNombre=['Ana',
            'Pedro',
            'María',
            'Rosa',
            'Sandra',
            'Celia']



'''for elemento in listaNombres:
    #if re.findall('^http',elemento): hace referencia a los que comienzan con http
    if re.findall('es$',elemento):#Hace referencia a los que terminan con el dominio .es
        print(elemento)

for i in listaCosas:
    if re.findall('cami[oó]n',i):#Nos permite encontrar un nombre, con o sin tilde
        print(i)'''

for i in listaNombre:
    if re.findall('[o-t]',i):#Nos permite encontrar un rango de letras (^o-t])--> con eso digo que devuelva los que no son esos
        print(i)
