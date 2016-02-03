#!/usr/bin/python3


def fibonacci():
    """ Generador de la secuencia Fibonacci..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
suma = 0
fibter = f.next()
while fibter < 4000000:
    if fibter % 2 == 0:
        suma += fibter

    fibter = f.next()


print("Resultado 0002:", suma)
