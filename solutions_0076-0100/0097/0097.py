#!/usr/bin/python
# -*- coding: utf-8 -*-


from datetime import datetime


def solution_0097():

    # primero calculamos los últimos 10 dígitos de 2^7830457
    n = 2
    for i in range(1, 7830457):
        n = n * 2
        n = int(str(n)[-10:])

    return int(str((n * 28433) + 1)[-10:])


start_time = datetime.now()

resultado = solution_0097()

print "Tiempo total: ", datetime.now() - start_time

print "Resultado de 0097: ", resultado
