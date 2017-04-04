# -*- coding: utf-8 -*-


def fibonacci():
    """ Generador de la secuencia Fibonacci..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def result():
    f = fibonacci()
    suma = 0
    fibter = next(f)
    # print(int(fibter))
    while fibter < 4000000:
        if fibter % 2 == 0:
            suma += fibter

        fibter = next(f)
    return suma
