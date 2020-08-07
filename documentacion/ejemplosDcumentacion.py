class Areas:
    def areaCuadrado(lado):
        ''' Calcula el area de un cuadrado elevenado el cuadrado pasandolo por parametros  '''
        return "El area del cuadrado es: " +str(lado*lado)

    def areaTriangulo(base,altura):
        return "El area de triángulo es: " +str((base*altura)/2)


print(Areas.areaTriangulo(2,7))
print(Areas.areaCuadrado.__doc__)#Me imprime los comentarios que puse dentro de la función

help(Areas.areaCuadrado)# de igual manera da más información de la funcion y su comentario

help(Areas)#Es una explicacion de la clase en general
# Se puede utilizar modulos y todo
