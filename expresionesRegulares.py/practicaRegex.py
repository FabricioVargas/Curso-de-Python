import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

'''if(re.search("aprender",cadena) is not None):#primer parametro es la palabra que estamos buscando
#el segundo es el texto en donde lo vamos a buscar, que en este caso es ña variable cadena
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")'''


#si encuenntra la palabra devuelve un objeto, sino devuelve none

textoBuscar="aprender"

textoEncontrar="Python"

textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start())# devuelve el numero donde se encuentre el
#primer caracter a buscar

print(textoEncontrado.end())# donde termina el caracter

print(textoEncontrado.span())# devuelve una tupla de donde comienza y termina la palabra a buscar en la cadena

print(len(re.findall(textoEncontrar, cadena)))# devuelve la cantidad de veces de que esta una palabra
