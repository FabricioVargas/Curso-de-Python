class carro():

    def __init__(self): #Forma de crear un método constructor en python
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4 #estoy encapsulando la variable ruedas para que no pueda ser accesida desde el exterior
        self.enmarcha=False
        # metiendo estos datos es el constructor hago constar que todos los elementos cunado inicien
        # van a tener estas caracteristicas

    def arrancar(self,arrancamos):# el argumento self siempre tiene que ir, es la palabra this
        self.enmarcha=arrancamos #aqui digo this.enmarcha=True

        if self.enmarcha:
            chequeo=self.__cehequeoInterno()
        if self.enmarcha and chequeo:
            return "El carro esta en marcha"
        elif self.enmarcha and chequeo==False:
            return "Algo ha idp en el chequeo, algo salio mal"
        else:
            return "El carro esta parado"

    def estado(self):
        print("El coche tiene " ,self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, " y un largo de ",
        self.largoChasis)

    def __cehequeoInterno(self): #Aqui estoy haciendo un metodo encapsulando
        print("Chequeo interno")

        self.gasolina="ok"
        self.aceite="mal"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False


miCarro=carro() #Instancia de la clase, no se utiliza el new como en otros lenguajes
print(miCarro.arrancar(True))
miCarro.estado()

print("----------------A continuacion creamos nuestro segundo objeto-----------------------------")

miCarro2=carro()
print(miCarro.arrancar(False))
miCarro2.estado()
