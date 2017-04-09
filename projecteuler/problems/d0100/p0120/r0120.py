# -*- coding: utf-8 -*-


def calc_resto_pe120(a, n):
    return ((((a - 1)**n) + ((a + 1)**n)) % (a*a))


def calc_max_resto_pe120(a):
    """ Para comprobar el ciclo, guardamos el primer valor para n = 1 """
    ciclo = calc_resto_pe120(a, 1)
    resto_max = 0
    es_ciclo = False
    n = 1

    while (not es_ciclo):
        n = n + 1
        resto = calc_resto_pe120(a, n)

        if resto > resto_max:
            resto_max = resto

        if resto == ciclo:
            es_ciclo = True

    return resto_max


def result():
    sumatorio = 0
    for a in range(3, 1001):
        sumatorio = sumatorio + calc_max_resto_pe120(a)

    return sumatorio
