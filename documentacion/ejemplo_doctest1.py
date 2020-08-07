def compruebaMail(mailUsuario):
    '''
    La función compruebaMail evalúa un mail recibiendo en busca de la
    @. Si tiene una @ es correcto, si tiene más de un @ es incorrecto
    si la @ está al final es incorrecto


    >>> compruebaMail('fabricio@gmail.com')
    True

    >>> compruebaMail('fabricio@gmail.com@')
    False

    >>> compruebaMail('fabriciogmail.com')
    False

    >>> compruebaMail('@fabriciogmail.com')
    False


    '''
    arroba=mailUsuario.count("@")
    if arroba!=1 or mailUsuario.rfind("@")==(len(mailUsuario)-1) or mailUsuario.find("@")==0:
        return False

    else:
        return True

import doctest
doctest.testmod()
