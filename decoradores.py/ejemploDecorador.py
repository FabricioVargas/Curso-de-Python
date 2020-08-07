
def funncionDecoradora(funcionParametro):
    def funcionInterior(*args):# *args nos dice que va a tener un numero indeterminado de parametros

        print("Vamos a realizar un cálculo")

        funcionParametro(*args)

        print("Hemos terminado el cálculo")

    return funcionInterior()





@funncionDecoradora#llamo a ejecutar la funcion decoradora en el programa
def sumar(num1, num2):

    print(num1+num2)

@funncionDecoradora
def resta(num1, num2):
    
    print(num1-num2)

sumar(10,2)
resta(10,5)
