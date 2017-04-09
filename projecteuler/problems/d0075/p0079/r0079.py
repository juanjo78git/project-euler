# -*- coding: utf-8 -*-

import os


def read_keylog(f):
    f = open(f, 'r')
    l = []


    for linea in f:
        l.append(int(linea))
    f.close()

    return l


def result():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'keylog.txt')
    
    keylogs = read_keylog(fichero)

    print(keylogs)

    return 0

