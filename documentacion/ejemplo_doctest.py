def areaTringulo(base,altura):

    '''
    Calcula el area de un triangula dado

    >>> areaTringulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTringulo(4,5)
    'El área del triángulo es: 10.0'

    >>> areaTringulo(9,3)
    'El área del triángulo es: 13.5'

    '''

    return "El área del triángulo es: " +str((base*altura)/2)

import doctest
doctest.testmod()# SI la funcion devuelve el resultado que se le puso todo va bien, si devuelve error es que algo esta mal
