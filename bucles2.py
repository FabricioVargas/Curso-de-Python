for i in range(5,10): # cuenta del 5 al 9. Si le pongo un valor más es de cuento en cuanto los muestra (5,50,3)
    print(f"valor de la variable {i} ") #con la f al inicio y el {i} al final permite imprimir el numero de la lista
    # lo que hace es que nos permite unir texto con variables

email=input("Correo electrónico: ")
a=0
p=0
for i in range(len(email)):
    if email[i]=="@":
        print("@")
        a=1
    if email[i]==".":
        print(".")
        p=1
if a==1 and p==1:
    print("correo bueno")
else:
    print("correo malo")
