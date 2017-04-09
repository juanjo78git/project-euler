# -*- coding: utf-8 -*-

import operator
import functools

from projecteuler import mymaths


def rad(n):
    if n == 1:
        return 1
    else:
        return functools.reduce(operator.mul, mymaths.numdivsprimes(n), 1)


def result():
    LIMITE = 100000
    E_NUMERO = 10000
    tupla = []
    radlist = []
    for n in range(1, LIMITE + 1):
        # if n % 1000 == 0:
        #     print n
        rd = rad(n)
        tupla.append(n)
        tupla.append(rd)
        radlist.append(tupla)
        tupla = []

    radlist.sort(key=operator.itemgetter(1))
    # print "Resultado para 0124: ", radlist[E_NUMERO - 1][0]
    return radlist[E_NUMERO - 1][0]
