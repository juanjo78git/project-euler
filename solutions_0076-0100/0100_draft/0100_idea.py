#!/usr/bin/python

# from __future__ import division
import math

def squares(num):
    """ Generador de cuadrados """
    a = 1
    n = num
    while True:
        yield a
        n = n + 1
        a = n ** 2

def get_first_square(n):
    """ no entiendo, pero este numero siempre es un cuadrado perfecto ... """
    return int(((n * (n - 1) * 4) + 1) ** 0.5)


# cuidado, que al final estoy sacando de un cuadrado a otra vez no cuadrado, etc etc
def get_n_from_square(square):
    """ a partir de un cuadrado, obtenemos su valor N --> square = 4N + 1 """
    # return ((square - 1) / 4)
    return int((1 + (square ** 0.5)) / 2)

def get_b_from_square(square):
    """ a partir de un cuadrado, obtenemos su valor N --> square = 4N + 1 """
    return ((square - 1) / 4)


# cuidado, que al final estoy sacando de un cuadrado a otra vez no cuadrado, etc etc
def exist_n_from_b(b):
    """ a partir de un cuadrado, obtenemos su valor N --> square = 4N + 1 """

    salida = False
    # print 'dentro de exist_n_from_b', b
    # return ((square - 1) / 4)
    x = 4 * b
    # print x
    y = x + 1
    # print y
    # ss = math.sqrt(
    z = math.sqrt(y)

    if z ** 2 == y:
        z_1 = z + 1

        w = z_1 / 2.0

        if int(w) * 2 == z_1:
            salida = True
        else:
            salida = False

    n = (1 + (((4 * b) + 1) ** 0.5)) / 2
    # if n.is_integer():
        # print b, str(n)
        # print n
        # print x, y, z, z ** 2
        # if z ** 2 == y:
            # print 'YE'
    # return int(n)


    # pero eso no garantiza por ahora nada :(
    # if z ** 2 == y:
    # if salida:
    # if n.is_integer():
        # return True
    # else:
        # return False
    return salida


"""
pendiente

quedaria empezar a sacar cuadrados y ver que esas tres funciones van bien...

"""

# sq = squares(1)
sq = squares(1999999999999)
n = 1
while True:


    s = sq.next()
    # print s

    b = get_b_from_square(s)
    # print b

    # bien, aqui llego bien, sin decimales rarunos
    # print b
    b_2 = b / 2
    # print 'bdos', b_2

    if exist_n_from_b((b_2)) and exist_n_from_b(b):
        # print s, b, get_n_from_square(s)
        print get_n_from_square(s)
