# -*- coding: utf-8 -*-

from projecteuler import mymaths


def es_capicula10_2(n):
    return (mymaths.isstringpalindrome(str(n))
            and mymaths.isstringpalindrome(bin(n)[2:]))


def result():
    LIMITE = 1000000

    s = 0
    for n in range(1, LIMITE):
        if es_capicula10_2(n):
            s += n

    return s
