# -*- coding: utf-8 -*-

# Optimum polynomial
# Problem 101
# If we are presented with the first k terms of a sequence it is impossible to
# say with certainty the value of the next term, as there are infinitely many
# polynomial functions that can model the sequence.
#
# As an example, let us consider the sequence of cube numbers. This is defined
# by the generating function,
# un = n3: 1, 8, 27, 64, 125, 216, ...
#
# Suppose we were only given the first two terms of this sequence. Working on
# the principle that "simple is best" we should assume a linear relationship
# and predict the next term to be 15 (common difference 7). Even if we were
# presented with the first three terms, by the same principle of simplicity,
# a quadratic relationship should be assumed.
#
# We shall define OP(k, n) to be the nth term of the optimum polynomial
# generating function for the first k terms of a sequence. It should be clear
# that OP(k, n) will accurately generate the terms of the sequence for n ≤ k,
# and potentially the first incorrect term (FIT) will be OP(k, k+1); in which
# case we shall call it a bad OP (BOP).
#
# As a basis, if we were only given the first term of sequence, it would be
# most sensible to assume constancy; that is, for n ≥ 2, OP(1, n) = u1.
#
# Hence we obtain the following OPs for the cubic sequence:
#
# OP(1, n) = 1	1, 1, 1, 1, ...
# OP(2, n) = 7n−6	1, 8, 15, ...
# OP(3, n) = 6n2−11n+6     	1, 8, 27, 58, ...
# OP(4, n) = n3	1, 8, 27, 64, 125, ...
# Clearly no BOPs exist for k ≥ 4.
#
# By considering the sum of FITs generated by the BOPs (indicated in red
# above), we obtain 1 + 15 + 58 = 74.
#
# Consider the following tenth degree polynomial generating function:
#
# un = 1 − n + n2 − n3 + n4 − n5 + n6 − n7 + n8 − n9 + n10
#
# Find the sum of FITs for the BOPs.

from sympy.solvers import solve
from sympy import Symbol
from sympy import sympify


def F(n):
    """ Función general que calcula la secuencia """
    v = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    # v = n**3
    return v


# [n:1 --> An + B - 1, n:2 --> An + B - 8]
# [a + b - 1, 2*a + b - 8]
def OP(g):
    """ Retorna una lista con las funciones antes de resolver
        Por ejemplo retornaría para n**3:
            [a + b - 1, 2*a + b - 8] """

    l = []

    for n in range(1, g + 1):
        s = ''
        letter = 'a'
        for i in range(g - 1, -1, -1):
            s += '{} * {} + '.format(n ** i, letter)
            letter = chr(ord(letter) + 1)

        s += '(- {})'.format(str(F(n)))

        l.append(s)
    return l


def FIT(grade):
    """ Retorna el FIT para grado g """
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    d = Symbol('d')
    e = Symbol('e')
    f = Symbol('f')
    g = Symbol('g')
    h = Symbol('h')
    i = Symbol('i')
    j = Symbol('j')
    n = Symbol('n')
    symbols = [a, b, c, d, e, f, g, h, i, j, n]

    # ok, como estamos en un grado g, tendremos g variables
    s = ''
    letter = 'a'
    for k in range(grade - 1, -1, -1):
        s += '{} * {} + '.format(n ** k, letter)
        letter = chr(ord(letter) + 1)

    # funcion para obtener el siguiente FIT
    f = sympify(s[0:-3])

    # calculo los valores para las variables A, B, C...
    # ... y las resolvemos resolver la ecuacion de OP
    r = solve(OP(grade), symbols)

    # añadimos a la solución el valor que tendrá n
    r[n] = grade + 1

    # retornamos el valor de la función f y valores r
    return f.subs(r)


def result():
    GRADE = 10
    # grado de la ecuación polinómica

    t = 0

    for n in range(1, GRADE + 1):
        t += FIT(n)

    return t