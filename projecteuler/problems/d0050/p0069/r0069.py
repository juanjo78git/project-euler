# -*- coding: utf-8 -*-

from projecteuler import mymaths



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
    n_max = 0
    n_div_phi_max = 0
    lprimes = genlprimes(LIMIT)

    for n in range(2, LIMIT):
        n_phi = phi(lprimes, n)
        n_div_phi_aux = n/float(n_phi)

        if n_div_phi_aux > n_div_phi_max:
                n_div_phi_max = n_div_phi_aux
                n_max = n

    # print "Resultado 0069: ", n_max
    return n_max
