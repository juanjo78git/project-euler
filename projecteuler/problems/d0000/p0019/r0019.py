# -*- coding: utf-8 -*-


diasmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def esbisiesto(y):
    return (y % 4 == 0 and not y % 100 == 0) or (y % 400 == 0)


def result():
    # desplazamiento, ya que el 1 de 1901 es martes
    dias = 2
    total = 0
    for y in range(1901, 2001):
        c = 1
        for dm in diasmes:
            while dias >= 7:
                dias = dias - 7

            if dias == 0:
                total += 1

            if dm == 28:
                if esbisiesto(y):
                    dm += 1

            dias = dm + dias
            c += 1

    return total
