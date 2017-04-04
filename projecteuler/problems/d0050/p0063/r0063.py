#!/usr/bin/python

total = 0

for num in range(1, 10):
    exp = 1
    salida = False
    while not salida:
        res = num ** exp
        lenres = len(str(res))
        if lenres < exp:
            salida = True
        else:
            if lenres == exp:
                total += 1
                exp += 1

print("Resultado 063:", total)
