#!/usr/bin/python

# from __future__ import division
import math
# import gmpy2


def squares(num):
    """ Generador de cuadrados """
    n = num
    while True:
        a = n ** 2
        yield n, a
        n = n + 1


def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


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
    
    if is_square(y):
        z = math.sqrt(y)
        z_1 = z + 1

        if z_1 % 2 == 0:
            salida = True
        else:
            salida = False

        # n = (1 + (((4 * b) + 1) ** 0.5)) / 2
    
    return salida


# cuidado, que al final estoy sacando de un cuadrado a otra vez no cuadrado, etc etc
def exist_n_from_i(i):
    """ a partir de un cuadrado, obtenemos su valor N --> square = 4N + 1 """

    return ((1 + i) % 2 == 0)


# sq = squares(4000)
# sq = squares(1000000000000)
sq = squares(999999999999)
while True:


    # i: numero
    # s: el cuadrado del numero
    i, s = sq.next()
    # print i, s

    # 4B + 1 = S
    b = get_b_from_square(s)
    # print b

    # bien, aqui llego bien, sin decimales rarunos
    # print b
    b_2 = b / 2
    # print 'bdos', b_2

    if exist_n_from_b((b_2)) and exist_n_from_i(i):
        # print s, b, get_n_from_square(s)
        print "resultado: ", get_n_from_square(s)
