import pickle
# Se van creado personas para almacenarse en el fichero permanentemente
class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero=genero
        self.edad = edad
        print("Se ha  creado una persona nueva con el nombre", self.nombre)

    def __str__(self):#Convierte en cadena de texto, nos permite llegara ver la información de la clase, si no se pone esto comienza a tirar numero por ser binario
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]#cargar la información personas y leer información personas

    def __init__(self): # Hago un constructor para inicializar el archivo externo
        listaPersonas=open("ficheroExterno","ab+")#agregar información binaria
        listaPersonas.seek(0) # el programa va a leer del cursor hacia adelante, entonces si el cursor
        # esta al final no va a leer a todas las personas, por eso se pone al inicio

        try:# se utiliza porque la primera vez no van a haber archivos cargados y daría error
            self.personas=pickle.load(listaPersonas) #Se hace un vuelco de la información, carga la información
            print("Se ha cargado {} personas del fichero externo ".format(len(self.personas)))
        except:
            print("El fichero está vacío")

        finally:# este se carga si o si, siempre se va a ejecutar
            listaPersonas.close()
            del(listaPersonas)


    def agregarPersonas(self,p):
        self.personas.append(p) #Agrego esa persona a la lista
        self.guaradarPersonasenFicherosExterno()

    def mostrarPersonas(self): # Se uso al inicio para ver si la clase personas estaba funcionando de la mejor manera
        for p in self.personas:
            print(p)

    def guaradarPersonasenFicherosExterno(self):
        listaPersonas=open("ficheroExterno","wb")# Escribe información binaria
        pickle.dump(self.personas, listaPersonas) #Volcar
        listaPersonas.close()
        del(listaPersonas)

    def mostrarInforFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()
p=Persona("Juan","Masculino",28)#Creamos una persona
miLista.agregarPersonas(p) #Una vez hecha la instancia llamo al metodo agregar para agregar a la persona a la lista
miLista.mostrarInforFicheroExterno()
