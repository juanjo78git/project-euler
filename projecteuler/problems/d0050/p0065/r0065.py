# -*- coding: utf-8 -*-

import fractions


def fracterm(k, n, d):
    nuevo_n = ((k * n) + d)
    nuevo_d = n
    nuevo_n = nuevo_n // fractions.gcd(nuevo_n, nuevo_d)
    nuevo_d = nuevo_d // fractions.gcd(nuevo_n, nuevo_d)
    return nuevo_n, nuevo_d


def genl_e():
    uno = False
    dos = False
    n = 0
    l = []
    for i in range(1, 150):
        if uno and dos:
            n = n + 2
            l.append(n)
            uno = False
            dos = False
        else:
            if not uno:
                uno = True
                l.append(1)
            else:
                dos = True
                l.append(1)

    return [2, 1, 2] + l[3:]


def n_fraccion(v):
    l = genl_e()
    d = 1
    n = 1
    for i in range(v - 1, -1, -1):
        n, d = fracterm(l[i], n, d)
    return n, d


def r65(v):
    # para cuadrar
    v = v - 1
    n, d = n_fraccion(v)

    # calculamos la suma del numerador
    s = 0
    for i in list(str(n)):
        s = s + int(i)

    # print "Resultado 0065:", s
    return s


def result():
    return r65(100)
