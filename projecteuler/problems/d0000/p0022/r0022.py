# -*- coding: utf-8 -*-

import os


def result():

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'names.txt')

    f = open(fichero, 'r')

    # leemos, limpiamos, partimos en lista y ordenamos
    names = f.read().replace('"', '').split(',')
    names.sort()

    i  = 1
    total = 0
    for name in names:
        # el orden de la letra es la letra menos la 'A' más 1
        total += sum([ord(x) - ord('A') + 1 for x in name]) * i
        i += 1

    return total
