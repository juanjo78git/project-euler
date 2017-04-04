# -*- coding: utf-8 -*-

import math


def es_sumfactx(n):
    """ indica si un número es suma de sus factoriales """
    if n < 10:
        return False

    s = 0
    for i in str(n):
        s += math.factorial(int(i))

    return s == n


def result():
    t = 0
    for n in range(1, 1000000):
        if es_sumfactx(n):
            t += n

    return t
