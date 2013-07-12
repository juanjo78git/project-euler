#!/usr/bin/python3

suma = 0
for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        suma += i

print("Resultado 0001: ", suma)
