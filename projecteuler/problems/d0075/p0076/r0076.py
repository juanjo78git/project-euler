# -*- coding: utf-8 -*-

# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two
# positive integers?


def r(vdestino, nodo, suma, total):
    """ valor destino, nodo de partida, suma actual, total de aciertos """
    for i in range(nodo, vdestino):
        if suma + i == vdestino:
            total = total + 1
            continue
        else:
            if suma + i > vdestino:
                continue
            else:
                total = r(vdestino, i, suma + i, total)
    return total


def result():
    NUMERO = 100
    # print "Resultado 0076:", r(NUMERO, 1, 0, 0)
    return r(NUMERO, 1, 0, 0)
