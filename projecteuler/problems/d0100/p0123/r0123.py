# -*- coding: utf-8 -*-

from projecteuler import mymaths


def get_resto(n, p):
    return (((p - 1) ** n) + (p + 1) ** n) % (p ** 2)


def result():
    MAXIMO = 10000000000

    # generador de primos
    primegen = mymaths.prime()

    n = 0
    while True:
        p = primegen.__next__()
        n += 1
        r = get_resto(n, p)
        if r > MAXIMO:
            break

    # print "Resultado de 0123 ", n
    return n
