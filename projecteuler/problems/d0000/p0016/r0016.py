#!/usr/bin/python

numero = 2**1000
suma = 0

for i in range(0, len(str(numero))):
    suma += int(str(numero)[i])

print "Resultado 0016: ", suma
