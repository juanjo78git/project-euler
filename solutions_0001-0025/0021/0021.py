#!/usr/bin/python2


def lista_divisores(n):
    lidiv = []
    for i in range(1, (n / 2) + 1):
        if (n % i == 0):
            lidiv.append(i)
    return lidiv


def sum_divisores(n):
    lidiv = lista_divisores(n)
    sumatorio = 0
    for div in lidiv:
        sumatorio += div
    return sumatorio

suma = 0
for n in range(1, 10000):
    if (n == sum_divisores(sum_divisores(n))):
        if (n != sum_divisores(n)):
            #lista_amigos.append(n)
            suma += n

print 'Resultado 0021: ', suma