def divide():
    try:
        op1=(float(input("Introduce el primer número: ")))#float para poder trabajar con decimales
        op2=(float(input("Introduce el segundo número: ")))#float para poder trabajar con decimales

        print("La division es: " + str(op1/op2))
    except:# execept es un solo general pero para el cliente no es bueno porque el no sabe que esta pasando
    # es mejor hacer una lista de except seguidos con cada uno de las execpciones que puede dar para hacerles
    #saber al usuario
        print("Ha ocurrido un error")

    finally:# permite que pase lo que pase siempre suceda, se puede utilizar para una conexion de bases de datos
        print("Calculo finalizado")

#divide()

def evaluacionEdad(edad):
    if edad<0:
        raise  typeError("no se permiten edades negativas")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "Cuidate..."
print(evaluacionEdad(18))
