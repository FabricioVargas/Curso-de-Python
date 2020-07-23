def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2): # Hago los try y catch
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede divir entre 0")
        return "Operacion errónea"

while True:
    try:#No pongan strings
        op1=(int(input("Introduce el primer n�mero: ")))

        op2=(int(input("Introduce el segundo n�mero: ")))

        break

    except ValueError:
        print("Los valores introducidos no son numeros. Intentalo de nuevo")

operacion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operaci�n no contemplada")


print("Operaci�n ejecutada.")
