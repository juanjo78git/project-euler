# -*- coding: utf-8 -*-

LIMITE = 100


def sumdigits(n):
    return sum([int(i) for i in str(n)])


def result():
    m = 0
    for a in range(1, LIMITE + 1):
        for b in range(1, LIMITE + 1):
            m = max(m, sumdigits(a ** b))

    return m
