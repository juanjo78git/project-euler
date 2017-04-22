# -*- coding: utf-8 -*-

# Leyendo un número de izquierda a derecha, si no hay dígitos que se vean
# superados por el dígito a su izquierda, se le denomina un creciente, por
# ejemplo, 134468.
#
# Del mismo modo, si ningún dígito es superado por los dígitos a la derecha, se
# denomina un número decreciente, por ejemplo, 66420.
#
# Vamos a denominar a un entero positivo que no crece ni decrece un número
# "variable", por ejemplo, 155349.
#
# Es evidente que no puede haber números variables inferiores a cien; sin
# embargo, algo más de la mitad de los números inferiores a mil (525) son
# variables. De hecho, el menor número para el que la proporción de números
# variables alcanza por primera vez 50% es 538.
#
# Curiosamente, los números variables son cada vez más comunes, y, para cuando
# llegan a 21780, su proporción es del 90%.
#
# Halla el menor número para el que la proporción de números variables es
# exactamente del 99%.

import math


def coef_b(n):
    """ funciona """
    return n*(n+1)*(n+2)*(n+3)*(n+4)*(n+5)*(n+6)*(n+7)*(n+8)//math.factorial(9)


def calc_n_bouncy(zeroes):
    """ total de números variables donde zeores: 10^zeroes """

    total = -1

    n_ant = 0
    nb_igual = 9
    for d in range(2, 2 + zeroes):
        n = coef_b(d)
        nb_decre = n - 10
        nb_incre = nb_decre - n_ant + 1
        # print(nb_igual, nb_decre, nb_incre)
        total += nb_igual + nb_decre + nb_incre
        n_ant = n

    return total


def result():

    # x ^ zeroes
    zeroes = 100
    return calc_n_bouncy(zeroes)
