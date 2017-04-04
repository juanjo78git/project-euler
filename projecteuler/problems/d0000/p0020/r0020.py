# -*- coding: utf-8 -*-

from projecteuler import mymaths


def result():
    f100 = mymaths.factorial(100)
    suma = 0

    for i in range(0, len(str(f100))):
        suma += int(str(f100)[i])

    return suma
