# -*- coding: utf-8 -*-


def result():
    LIMITE = 1000

    t = 0
    for n in range(1, LIMITE + 1):
        t += n ** n

    return int(str(t)[-10:])
