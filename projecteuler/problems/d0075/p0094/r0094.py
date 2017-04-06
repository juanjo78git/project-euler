# -*- coding: utf-8 -*-

# Es fácil probar que no existe ningún triángulo equilátero con lados de
# longitud entera y área entera. Sin embargo, el triángulo casi equilátero
# 5-5-6 tiene una área de 12 unidades cuadradas.
#
# Vamos a definir un triángulo casi equilátero como un triángulo en el que dos
# lados son iguales y el tercero no difiere en más de una unidad.
#
# Halla la suma de los perímetros de todos los triángulos casi equiláteros con
# lados de longitud entera, área entera y cuyos perímetros no excedan mil
# millones (1.000.000.000).

import math


def heron(a, b, c):
    c1 = (a + (b + c)) * (c - (a - b)) * (c + (a - b)) * (a + (b - c))
    c2 = int(math.sqrt(c1))
    # la precisión deja que desear, yo pensaba que esto sería la bomba...
    if (c2 * c2) != c1:
        return -0.5
    else:
        return c2 / 4


def perimetro(a, b, c):
    return a + b + c


def entero(a):
    return int(a) == a


def result():
    LIMITE = 1000000000
    n = 2
    sp = 0
    r1 = True
    r2 = True

    ## podría meter cada sección en un hilo, así vamos el doble de rápidos
    while r1 or r2:

        p = perimetro(n, n, n - 1)
        # if p % 1000000 == 0:
        #     print p

        if p <= LIMITE:
            a = heron(n, n, n - 1)
            if entero(a):
                # print n, n - 1
                sp += p
        else:
            r1 = False

        p = perimetro(n, n, n + 1)

        if p <= LIMITE:
            a = heron(n, n, n + 1)
            if entero(a):
                # print n, n + 1
                sp += p
        else:
            r2 = False

        n += 1

    return sp
