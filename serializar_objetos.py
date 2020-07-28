import pickle
class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    #Comportamientos
    def arrancar(self):
        self.enmarcha=True
    def accelerar(self):
        self.acelera=True
    def frenar(self):
        self.frenar=False
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: " ,self.modelo, "\nMarcha: " ,self.enmarcha, "\nAcelera: " ,self.acelera, "\nFrena: " ,self.frena)


coche1=Vehiculos("Honda","MX5")
coche2=Vehiculos("Toyota","MX4")
coche3=Vehiculos("Suzuki","MX3")

coches=[coche1, coche2, coche3]

fichero=open("losChoces","wb")#escritura de bytes
pickle.dump(coches,fichero)
fichero.close()
del (fichero)# se borra el fichero

ficheroApertura=open("losChoces","rb")
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for i in misCoches:
    print(i.estado())
