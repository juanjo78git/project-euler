# -*- coding: utf-8 -*-

import itertools


def result():
    # el generador...
    g = itertools.permutations(range(0, 10))

    c = 0
    while c != 1000000:
        result = g.__next__()
        c += 1

    return ''.join([str(x) for x in result])
