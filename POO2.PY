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

class furgoneta(Vehiculos):# hereda de la clase vehículos
    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class moto(Vehiculos): #aqui creo una herencia
    #pass me deja hacer un metodo vacio para que no me de error
    hcaballito=""
    def caballito(self):# Metodo propio de la clase moto
        self.hcaballito="Voy llanteando la bichilla"
        return self.hcaballito

class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True


# ----------------------Instancias-------------------------------------

miMoto=moto("Honda","CBR")
miMoto.estado()
print(miMoto.caballito())


mifurgoneta=furgoneta("Renault","Kangoo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))


class bicicletaElectrica(VElectricos,Vehiculos): #Herencia multiple, la primer clase es la que domina más por aquello
# de recibir parametros y cosas así, en este caso no lleva parametros porque el VElectrico no recibe nada
    pass

miBici=bicicletaElectrica("Honda",2012)
