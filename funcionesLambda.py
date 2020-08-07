# lambda se puede decir que son abreviaciones

'''def areaTriangulo(base,altura):
    return (base*altura)/2'''


#funciones lambda

areaTriangulo= lambda base,altura: (base*altura)/2

print(areaTriangulo(5,7))

valor=lambda comision: "¡{}! $".format(comision)

print(valor(15585))
