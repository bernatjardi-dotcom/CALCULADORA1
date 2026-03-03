def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    suma = suma(2,3)
    print(suma)
    resta = resta(3,4)
    print(resta)
    multiplicacion = multiplicacion(3,4)
    print(multiplicacion)
    division = division(3,4)
    print(division)
