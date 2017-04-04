# -*- coding: utf-8 -*-


def result():
    t = 1
    n = 1
    for s in range(2, 1001, 2):
        for i in range(0, 4):
            n = n + s
            t += n

    return t
