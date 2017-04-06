# -*- coding: utf-8 -*-


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

        # if n % 100000 == 0:
        #     print n

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


def result():
    return solution_0092()
