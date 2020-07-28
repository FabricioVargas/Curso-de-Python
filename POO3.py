class Persona():
    def __init__(self,nombre,edad,Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia
    def descripcion(self):
        print("Nombre: " ,self.nombre, "Edad: " ,self.edad, "Lugar residencia: " , self.Lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre,edad,residencia):

        super().__init__(nombre,edad,residencia)# super llama al metodo de la clase padre que es init
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: " , self.salario, "Antiguedad: " , self.antiguedad)



fabricio=Empleado(1500,15,"Fabricio",23,"Puente") #Si no pongo la variable super()esta instruccion me da error porque no reconoce
#los valores que se necesitan en la clase persona
fabricio.descripcion()

print(isinstance(fabricio, Empleado)) #Me dice las instacias creadas a cual clase pertenece, devuelve true si efectivamente pertenece
