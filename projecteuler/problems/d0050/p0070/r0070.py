# -*- coding: utf-8 -*-

from projecteuler import mymaths

#LIMIT = 100


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


def numperm(n1, n2):
    return (sorted(str(n1)) == sorted(str(n2)))


def result():
    LIMIT = 10000000
    n_min = 0
    n_div_phi_min = LIMIT
    lprimes = genlprimes(LIMIT)

    # print "generacion de lista de primos terminada."

    for n in range(2, LIMIT):

        # if n % 100000 == 0:
        #     print "vamos por: ", n

        n_phi = phi(lprimes, n)

        if numperm(n, n_phi):

            n_div_phi_aux = n/float(n_phi)

            if n_div_phi_aux < n_div_phi_min:
                n_div_phi_min = n_div_phi_aux
                n_min = n

    # print "Resultado 0070: ", n_min
    return n_min
