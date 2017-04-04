# -*- coding: utf-8 -*-


# generamos el iterador
def iter14(n):
    while True:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        yield n


def num_terminos_iter14(n):
    it = iter14(n)
    total = 1
    e = 0
    while e != 1:
        e = it.__next__()
        total += 1

    return total


def result():
    maxterminos = 0
    n = 0
    limite = 1000000

    for i in range(2, limite):
        calc = num_terminos_iter14(i)
        if calc > maxterminos:
            maxterminos = calc
            n = i

    return n
