# -*- coding: utf-8 -*-

#Por ejemplo, √19 tiene la expansión en fracciones continuas
#que es recurrente cada 6 fracciones. El término inmediatamente anterior al
#punto en el que se repite es 170/39 y la teoría de Lagrange dice que

#x = 39, y = 170

#será la solución más pequeña a la ecuación de Pell

#19x2 + 1 = y2.

#http://hojaynumeros.blogspot.com.es/2010/02/ecuacion-de-pell.html


def contfrac(r, a, b):
    ''' solo para el calculo de las fracciones '''
    # ejemplo, el anterior paso se había quedado así
    # 1 + (raiz(23) - 3 / 7)
    # i = 1
    # a = 3
    # b = 7
    #
    # ahora quiero para el siguiente paso la fraccion:
    # 7 / raiz(23) - 3
    # b / raiz(23) - a
    newi = int(b / ((r ** 0.5) - a))
    newb = r - (a * a)
    # b es divisor de newb
    newb = newb / b
    z = newi * newb
    newa = a - z
    #print r, newi, newa, newb
    return newi, (newa * -1), newb


def fracxy(i, xy0, xy1):
    return (i * xy1) + xy0


def espell(x, y, d):
    if (x**2) - (d*(y**2)) == 1:
        return True
    else:
        return False


def calcfrac(r):
    if r ** 0.5 == int(r ** 0.5):
        return -1
    i = int(r ** 0.5)
    x0 = 0
    x1 = 1
    y0 = 1
    y1 = 0

    # primera fraccion...
    x, y = fracxy(i, x0, x1), fracxy(i, y0, y1)
    x0 = x1
    x1 = x
    y0 = y1
    y1 = y

    # primera llamada
    i, a, b = contfrac(r, int(r ** 0.5), 1)

    x, y = fracxy(i, x0, x1), fracxy(i, y0, y1)
    x0 = x1
    x1 = x
    y0 = y1
    y1 = y

    # si es pell, osea, solución
    if espell(x, y, r):
        return x

    while True:
        i, a, b = contfrac(r, a, b)
        x, y = fracxy(i, x0, x1), fracxy(i, y0, y1)

        x0 = x1
        x1 = x
        y0 = y1
        y1 = y

        if espell(x, y, r):
            break
    return x


def result():
    LIMITE = 1000

    maxx = 0
    res = 0

    for i in range(1, LIMITE + 1):
        x = calcfrac(i)

        if x > maxx:
            maxx = x
            res = i

    # print("Resultado 0066:", res)
    return res
