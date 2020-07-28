from io import open #poder abrir un archivo externo video 38 y 39

archivo_texto=open("archivo.txt","w")# primer valor el nombre del archivo y el segundo permiso de escribir
# sino existe el archivo.text entonces en la carpeta raiz se crea por defecto
frase="Estupendo dia para estudiar Python \n el miércoles"
archivo_texto.write(frase)#escribo en el archivo externo la frase que cree
archivo_texto.close()# cerramos el archivo_texto

#Pasos
#crear
#Manipular
#Cerrar

#-----------------Leer archivo-------------------------------

from io import open #poder abrir un archivo externo

archivo_texto=open("archivo.txt","r")# primer valor el nombre del archivo y el segundo permiso de leer
texto=archivo_texto.read()#leeo el archivo externo
archivo_texto.close()# cerramos el archivo_texto

print(texto)

#readlines: leer el texto linea a linea y lo almacena en una lista, eso es más facil de manipular y ordenar

#------------------------readlines---------------------------------
from io import open #poder abrir un archivo externo

archivo_texto=open("archivo.txt","r")# primer valor el nombre del archivo y el segundo permiso de leer
lineas_texto=archivo_texto.readlines()#lineas de texto se vuelve una lista donde esta cada linea de texto
archivo_texto.close()
print(lineas_texto[0])#imprimo una la primer linea de la lista

#------------------------append---------------------------------Modo Agregar
from io import open #poder abrir un archivo externo

archivo_texto=open("archivo.txt","a")# primer valor el nombre del archivo y el segundo permiso append
archivo_texto.write("\n siempre es una buena ocacion para estudiar python")
archivo_texto.close()

# Posicionar el puntero en python seek

#---------------------------seek------------------------
from io import open #poder abrir un archivo externo

archivo_texto=open("archivo.txt","a")# primer valor el nombre del archivo y el segundo de leer
print(archivo_texto.read())
archivo_texto.seek(0)#pone el puntero en esa posicion por defecto, si quito esta opcion no se imprime dos veces
# ya que imprime una vez y el cursor se va a lo ultimo y con esta accion devuelvo al cursor al inicio
#por lo cual lo vuelve a imprimir
print(archivo_texto.read())# si le ,eto parametros al read el vva a leer hasta el numero de caracteres
# que se le asigne dentro de los paretesis


archivo_texto=open("archivo.txt","r+")# archivo de lectura y escritura
