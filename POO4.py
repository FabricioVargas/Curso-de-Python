class carro():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


def desplazamientoVehiculo(vehiculo): #Segun el vehiculo llama al desplazamiento que le corresponde
# esto es polimosfirmo son como objeto se puede amoldar a diferentes formas cambiando su comportamiento
    vehiculo.desplazamiento()

miVehiculo= camion() #Objeto que voy a enviar a la definicion de polimorfismo
desplazamientoVehiculo(miVehiculo)
