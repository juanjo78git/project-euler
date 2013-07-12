#!/usr/bin/python

fichero = '0013.txt'

f = open(fichero, 'r')
total = 0

for linea in f:
    total += int(linea)
f.close()

print "Resultado 0013: ", str(total)[:10]
