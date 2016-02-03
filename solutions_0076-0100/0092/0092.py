#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


def chain92(n):
    """ Generador de la secuencia cadena 0092 """
    a = n
    while True:
        yield a
        t = 0
        for c in str(a):
            t += int(c) ** 2
        a = t


def solution_0092():

    total_89 = 0

    for n in range(1, 10000000):

        if n % 100000 == 0:
            print n

        # el generador
        c = chain92(n)

        while True:
            r = c.next()
            if r == 1:
                break
            elif r == 89:
                total_89 += 1
                break

    return total_89

start_time = datetime.now()

resultado = solution_0092()

print "Tiempo total: ", datetime.now() - start_time

print "Resultado de 0092: ", resultado
