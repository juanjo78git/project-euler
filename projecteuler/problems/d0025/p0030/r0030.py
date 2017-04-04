# -*- coding: utf-8 -*-


def es_sumpotx(n, p):
    """ indica si un número es suma de su pontencia p, importante: SUMA, es
        necesario que el número sea por tanto mayor que 9 """
    if n < 10:
        return False

    s = 0
    for i in str(n):
        s += int(i) ** p

    return s == n


def result():
    t = 0
    for n in range(1, 1000000):
        if es_sumpotx(n, 5):
            t += n

    return t
