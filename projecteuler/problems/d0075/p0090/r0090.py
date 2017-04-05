# -*- coding: utf-8 -*-

# Each of the six faces on a cube has a different digit (0 to 9) written on it;
# the same is done to a second cube. By placing the two cubes side-by-side in
# different positions we can form a variety of 2-digit numbers.
#
# For example, the square number 64 could be formed:
#
#
# In fact, by carefully choosing the digits on both cubes it is possible to
# display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36,
# 49, 64, and 81.
#
# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
# one cube and {1, 2, 3, 4, 8, 9} on the other cube.
#
# However, for this problem we shall allow the 6 or 9 to be turned upside-down
# so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
# for all nine square numbers to be displayed; otherwise it would be impossible
# to obtain 09.
#
# In determining a distinct arrangement we are interested in the digits on each
# cube, not the order.
#
# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5} {1, 2, 3, 4, 5, 6} is
# distinct from {1, 2, 3, 4, 5, 9}
#
# But because we are allowing 6 and 9 to be reversed, the two distinct sets in
# the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for
# the purpose of forming 2-digit numbers.
#
# How many distinct arrangements of the two cubes allow for all of the square
# numbers to be displayed?

import itertools


def prepare_list(t):
    """ pasamos la tupla a lista, y si en la lista había un 6, ponemos un 9 """
    l = list(t)
    if 6 in l and 9 not in l:
        l.append(9)
    if 9 in l and 6 not in l:
        l.append(6)
    return l


def verificar_cuadrados(t1, t2):
    # la lista de caudrados (un poco de trampa!)
    cuadrados = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

    c1 = prepare_list(t1)
    c2 = prepare_list(t2)

    for cuadrado in cuadrados:
        if ((not int(cuadrado[0]) in c1 or not int(cuadrado[1]) in c2) and
                (not int(cuadrado[0]) in c2 or not int(cuadrado[1]) in c1)):
            return False
    return True


def result():
    r = []
    for t1 in itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6):
        for t2 in itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6):
            if verificar_cuadrados(t1, t2):

                n1 = ''.join(str(x) for x in list(t1))
                n2 = ''.join(str(x) for x in list(t2))

                # mira, para no liarme, los meto dos veces, de un lado y de
                # otro, así aseguro que no los tenemos dos veces, luego el
                # resultado será el valor entre dos

                if n1 + '-' + n2 not in r:
                    r.append(n1 + '-' + n2)
                    r.append(n2 + '-' + n1)

    # print "Resultado 0090: ", len(r) / 2
    return len(r) / 2
