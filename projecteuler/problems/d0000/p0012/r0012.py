# -*- coding: utf-8 -*-

from projecteuler import mymaths


def result():
    # numero de divisores minimo que buscamos
    nmindivs = 500

    t = mymaths.trianglenumber()

    while True:
        n = t.__next__()
        if mymaths.numdivs(n) > nmindivs:
            break

    return n
