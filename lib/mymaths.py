# -*- coding: utf-8 -*-
# mymaths algunas funciones que uso mucho


def ispalindrome(n):
    """ Retorna si un numero es palindromo """
    s = str(n)
    for i in range(0, len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True


def isprime(n):
    """ Retorna si un numero es primo """
    if n == 1:
        return False

    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False

    return True


def ispythagoreantriplet(a, b, c):
    """ Retorna si es una tripleta pitagorica """
    return a**2 + b**2 == c**2


# MUY rapida, eliminamos las demas
def numdivs(n):
    """ Devuelve el total de divisores de un numero """
    # http://mathschallenge.net/library/number/number_of_divisors
    # Basado en:
    # n = p^a * q^b ...
    # d(n) = (a+1)*(b+1)...
    t = 1
    d = 2
    numd = 0            # numero de veces que usamos d
    while n != 1:
        if n % d == 0:
            n = n / d
            numd += 1

            # caso de salida, vaya chapuza, que mal estruturado
            if n == 1:
                t = t * (numd + 1)
        else:
            # si d divide al numero...
            if numd > 0:
                t = t * (numd + 1)

            d += 1
            numd = 0
    return t


def lnumdivs(n):
    """ lista de divisores de un número """
    lidiv = []
    for i in range(1, (n / 2) + 1):
            if (n % i == 0):
                    lidiv.append(i)
    return lidiv


def numdivsprimes(n):
    """ lista de primos que son divisibles por el numero """
    ldiv = []
    p = prime()
    d = p.next()
    while n != 1:
        r, m = divmod(n, d)
        if m == 0:
            n = r
            if d not in ldiv:
                ldiv.append(d)
        else:
            d = p.next()

    return ldiv


def factorial(x):
    """ Factorial recursivo """
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


# GENERADORES _________________________________________________________________


def fibonacci():
    """ Generador de la secuencia Fibonacci"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    """ Generador de secuencia numeros primos"""
    p = 2
    while True:
        yield p

        while (not isprime(p + 1)):
            p += 1

        p = p + 1


def trianglenumber():
    """ Generador de secuencia numeros triangulo """
    n = 1
    i = 1
    while True:
        yield n
        n, i = n + i + 1, i + 1


# LISTAS ______________________________________________________________________
#

def genlprimes(n):
    """ genera una lista de primos que pueda dividir n """
    l = []
    p = prime()
    myprime = p.next()
    # quiero una lista de primos que dividan a n, por lo tanto con
    # buscar solo la mitad me va bien
    limit = n + 1
    while myprime < limit:
        l.append(myprime)
        myprime = p.next()

    return l
