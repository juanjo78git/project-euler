#!/usr/bin/python


# Funcion para el factorial
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def n_C_r(n, r):
    return (factorial(n) / (factorial(r) * factorial(n - r)))

contador = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        if n_C_r(n, r) > 1000000:
            contador = contador + 1

print contador
