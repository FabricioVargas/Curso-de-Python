import re

#patron de busquedas siempre al inicio de el texto

nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="Maria Lopez"

numero1="12345"#\d
numero2="09876"

'''if re.match("Sandra",nombre1,re.IGNORECASE):#IGNORECASE permite que no haya problemas si es mayúscula o minúscula
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")'''

if re.match("\d",numero1):#Nos permite encontrar si comienza con numeros
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")


if re.search("Lopex",numero1):#Busca eso no solo al inicio sino en toda la cadena
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")
