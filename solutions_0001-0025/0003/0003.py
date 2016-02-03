#!/usr/bin/python3


def isprime(n):
    if n == 1:
        return False

    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


numero = 600851475143

divisor = 1
divisor_mayor = 0
salida = False

while not salida:

    divisor += 1

    if isprime(divisor):

        while (numero % divisor == 0):
            numero = numero / divisor
            divisor_mayor = divisor

    if numero < divisor:
        salida = True


print ("Resultado 0003: ", divisor_mayor)
