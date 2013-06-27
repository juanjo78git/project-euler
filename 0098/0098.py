# -*- coding: utf-8 -*-

#!/usr/bin/python

from datetime import datetime


def maxlenwords(words):
    maxi = 0
    for w in words:
        if maxi < len(w):
            maxi = len(w)
    return maxi


def getlistsquares(maximo):
    l = []
    n = 1
    square = n ** 2
    while len(str(square)) <= maximo:
        l.append(square)
        n = n + 1
        square = n ** 2

    return l

# controlamor el tiempo de ejecución
start_time = datetime.now()

f = open('words.txt', 'r')

words = f.readline().replace('"', '').split(',')

maxi = 0

for w in words:
    if maxi < len(w):
        maxi = len(w)

print maxi













print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0098: "
