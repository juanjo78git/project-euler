# -*- coding: utf-8 -*-

from projecteuler import mymaths


def result():
    # el iterador
    p = mymaths.prime()

    limite = 10001

    for _ in range(1, limite):
        p.__next__()

    return p.__next__()
