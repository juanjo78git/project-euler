#!/usr/bin/python3


limite = 100
sumacuadrados = 0
cuadradossuma = 0

for i in range(1, limite + 1):
    sumacuadrados += i**2
    cuadradossuma += i

resta = cuadradossuma**2 - sumacuadrados


print ("Resultado 0006: ", resta)
