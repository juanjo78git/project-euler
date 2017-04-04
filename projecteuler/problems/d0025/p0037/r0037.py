# -*- coding: utf-8 -*-


def isprime(n):
    if n == 1:
        return False

    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def is37(n):
    # Vemos si el numero es primo
    if (isprime(n)):
        cadena = str(n)
        for i in range(len(cadena) - 1, 0, -1):
            if not isprime(int(cadena[i:len(cadena)])):
                return False

        for i in range(1, len(cadena)):
            if not isprime(int(cadena[0:i])):
                return False

        # si hemos pasado todas la pruebas
        return True
    # no hemos pasado todas las pruebas
    return False


def result():
    numeros = 0
    suma = 0
    n = 9
    while (numeros != 11):

        n += 2

        if (is37(n)):
            numeros += 1
            suma += n

    return suma
