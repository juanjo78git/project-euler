#!/usr/bin/python2

from decimal import Decimal


def triangulo(n):
    return (n*(n + 1)) / 2


def pentagono(n):
    return (n * ((3 * n) - 1)) / 2


def hexagono(n):
    return n * ((2 * n) - 1)


def inv_pentagono(n):
    x_pos = (1 + Decimal(1 + 24*n).sqrt()) / 6

    if (x_pos != int(x_pos)):
        return -1
    else:
        return int(x_pos)


def inv_hexagono(n):
    x_pos = (1 + Decimal(1 + 8*n).sqrt()) / 4

    if (x_pos != int(x_pos)):
        return -1
    else:
        return int(x_pos)


#consideramos a >= b >= c

#completa fuerza bruta
for a in range(286, 1000000):
    res_a = triangulo(a)

    inv_h = inv_hexagono(res_a)

    if (inv_h == a):

        inv_p = inv_pentagono(res_a)

        if (inv_h == inv_p):
            print res_a, a
            break
