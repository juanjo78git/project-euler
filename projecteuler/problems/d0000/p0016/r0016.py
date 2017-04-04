# -*- coding: utf-8 -*-


def result():
    numero = 2**1000
    suma = 0

    for i in range(0, len(str(numero))):
        suma += int(str(numero)[i])

    return suma
