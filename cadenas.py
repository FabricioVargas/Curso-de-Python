nombreUsuario=input("Introduce el nombre de usuario :")

print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())


edad=input("Introduce la edad: ")
print(edad.isdigit())# devuelve un true si es un digito y false si no

while(edad.isdigit()==False):
    print("Por favor introduce un valor numerico")
    edad=input("Introduce la edad: ")

if(int(edad)<18):
    print("Puede pasar")
else:
    print("No puede pasar")
