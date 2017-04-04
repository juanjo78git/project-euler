# -*- coding: utf-8 -*-


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
    return (newa * -1), newb


def calcfrac(r):
    if r ** 0.5 == int(r ** 0.5):
        return -1

    # primera llamada
    firsta, firstb = contfrac(r, int(r ** 0.5), 1)
    a, b = firsta, firstb
    count = 0
    while True:
        a, b = contfrac(r, a, b)
        count += 1
        if firsta == a and firstb == b:
            break
    return count


def result():
    LIMITE = 10000

    res = 0
    # print calcfrac(23)
    for i in range(2, LIMITE + 1):
        c = calcfrac(i)
        if c != -1 and c % 2 != 0:
            res += 1

    # print("Resultado 0062:", res)
    return res
