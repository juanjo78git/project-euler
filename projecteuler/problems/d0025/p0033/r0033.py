# -*- coding: utf-8 -*-

from projecteuler import mymaths


def divisores_euclides(n):
    divisores = []
    for i in range(2, int(n/2+1)):
        # print(i)
        while n % i == 0:
            # print "ok"
            n = n / i
            divisores.append(i)

    return divisores


def numeros_que_comparten(n1, n2):
    l = []
    for i in str(n1):
        if i in str(n2):
            l.append(int(i))

    l.sort()
    return l


def delete_number(number, n):
    s = str(number).replace(str(n), '')

    if len(s) == 0:
        s = str(n)

    return int(s)


def es_p33(numerador, denominador):
    comparten = numeros_que_comparten(numerador, denominador)

    if 0 in comparten:
        return False

    for c in comparten:
        new_numerador = delete_number(numerador, c)
        new_denominador = delete_number(denominador, c)

        return ((new_numerador * denominador) == (numerador * new_denominador))


def result():
    total = mymaths.Fraccion(1, 1)
    for numerador in range(10, 99):
        for denominador in range(10, 99):
            if numerador < denominador:
                if es_p33(numerador, denominador):
                    total = total * mymaths.Fraccion(numerador, denominador)

    total.simplify()

    return total.d
