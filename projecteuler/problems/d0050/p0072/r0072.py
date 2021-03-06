# -*- coding: utf-8 -*-

from projecteuler import mymaths

# parto del codigo de 0070, algunas pequenas modificaciones y ya lo tengo
# totalmente operativo y unos tiempos de menos de 5 minutos en pypy


def genlprimes(n):
    """ genera una lista de primos que pueda dividir n """
    l = []
    p = mymaths.prime()
    prime = p.__next__()
    # quiero una lista de primos que dividan a n, por lo tanto con
    # buscar solo la mitad me va bien
    limit = n + 1
    while prime < limit:
        l.append(prime)
        prime = p.__next__()

    return l


def numdivsprimes(lprimes, n):
    """ lista de primos que son divisibles por el numero n, pasandole la lista
        de primos """
    ldiv = []

    if n in lprimes:
        ldiv.append(n)
        return ldiv

    np = 0
    d = lprimes[np]
    while n != 1:
        r, m = divmod(n, d)
        if m == 0:
            n = r
            if d not in ldiv:
                ldiv.append(d)
        else:
            np += 1
            d = lprimes[np]

    return ldiv


def phi(lprimes, n):
    """ funcion phi, a partir de un listado de primos, para facilitar """

    ldivs = numdivsprimes(lprimes, n)
    arriba = 1
    abajo = 1

    for div in ldivs:
        arriba = (div - 1) * arriba
        abajo = div * abajo

    return (n * arriba) / abajo


def result():
    LIMIT = 1000000
    lprimes = genlprimes(LIMIT)
    n_sum = 0

    # print "generacion de lista de primos terminada."

    for n in range(2, LIMIT + 1):

        n_sum += phi(lprimes, n)

    # print "Resultado 0072: ", n_sum
    return int(n_sum)
