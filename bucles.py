email=False
miEmail=input("Introduce su correo electrónico: ")
for i in miEmail: #Aqui lo que sucede es que reccore caracter por caracter
    if (i=="@"):
        for i in miEmail:
            if (i=="."):
                email=True

if (email==True):
    print("Email correcto")
else:
    print("Email incorrecto")

#print("Hola", end=" ") hace la impresion de los archivos en una sola linea


ca=0
cp=1
c=input("Email:")
co=input("Contraseña:")
for i in c:
 if(i=="@"):
  ca+=1
 if(i=="."):
  cp+=1
if(ca==1 and cp>1):
 print("Correcto")
else:
 print("Incorrecto")


for i in range(5): # lo que genera es una lista de numeros 0,1,2,3,4
    print("hola")
