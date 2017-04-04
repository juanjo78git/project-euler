# -*- coding: utf-8 -*-

import itertools
import os


def file2list(path):
    f = open(path)
    return f.read().replace('\n', '').split(",")


def lisxor2string(lxor):
    laux = []
    for i in lxor:
        laux.append(chr(i))
    return "".join(laux)


# algunas letras comunes para buscar
def testwords(s):
    words = ["and", "the", "beginning", "who"]

    for w in words:
        if s.find(w) == -1:
            return False

    return True


def sumASCIIstring(s):
    suma = 0
    for i in range(0, len(s)):
        suma += ord(s[i])

    return suma


def result():

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(ROOT_DIR, 'cipher1.txt')
    lis = file2list(fichero)

    # xor es ^

    abc = "abcdefghijklmnopqrstuvwxyz"

    # obtenemos todos los posibles valores de las tres letras en minuscula
    for i in itertools.product(abc, repeat=3):
        x = "".join(i)

        lisxor = []
        for j in range(0, len(lis)):
            lisxor.append(int(lis[j]) ^ ord(x[j % 3]))

        # vamos a intentar pintar el lisxor pero como cadenas
        # print(lisxor)
        s = lisxor2string(lisxor)

        # print(x, s, lisxor, lis)
        # print(x)

        if testwords(s):
            # print(x)
            # print(s)
            # print(sumASCIIstring(s))
            return sumASCIIstring(s)
