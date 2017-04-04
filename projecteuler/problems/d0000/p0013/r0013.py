# -*- coding: utf-8 -*-

import os


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, '0013.txt')

    f = open(fichero, 'r')
    total = 0

    for linea in f:
        total += int(linea)
    f.close()

    return str(total)[:10]
