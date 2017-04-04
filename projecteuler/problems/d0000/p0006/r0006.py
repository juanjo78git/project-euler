# -*- coding: utf-8 -*-


def result():
    limite = 100
    sumacuadrados = 0
    cuadradossuma = 0

    for i in range(1, limite + 1):
        sumacuadrados += i**2
        cuadradossuma += i

    return cuadradossuma**2 - sumacuadrados
