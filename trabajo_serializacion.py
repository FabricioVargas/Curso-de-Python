import pickle

lista_nombre=["Pedro","Ana","María","Isabel"]

fichero_binario=open("lista_nombre","wb")# Se acaba de escribir un archivo esterno de escritura binaria

pickle.dump(lista_nombre, fichero_binario)#volcamos el archivo, parametros: informacion a volcar y fichero al que qeuremos volcar

fichero_binario.close()
# se debe crear un archivo en la raiz con el nombre lista_nombre
del (fichero_binario) # se borra en memoria

# ---------------------Lo rescatamos y leemos la información de él-------------------------------
import pickle
fichero=open("lista_nombre","rb")# aqui le digo que lea información vinaria
lista=pickle.load(fichero)#cargo la lista
print(lista)
