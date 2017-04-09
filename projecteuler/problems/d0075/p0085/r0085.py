# -*- coding: utf-8 -*-


def calc_cuadraditos(x, y):
    t = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            t += i * j
    return t


def result():
    CUADRADOS = 2000000

    near = 0
    x_res = 0
    y_res = 0
    for x in range(1, 100):
        for y in range(1, 100):
            nc = calc_cuadraditos(x, y)
            if nc > CUADRADOS:
                break

            if nc > near:
                near = nc
                x_res = x
                y_res = y

    # print "Resultado de 0085: ",
    return (x_res * y_res)
