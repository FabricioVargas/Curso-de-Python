for i in "python":
    if i=="h":
        continue #corta el flujo de ejecucion y no hace el print, lo devuelve al for
    print(f"viendo la letra {i}")

nombre="Fabricio Vargas"# Voy a contar solo las letras y no los espacios en blanco

contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)
