# -*- coding: utf-8 -*-

#Project Euler 0080
#It is well known that if the square root of a natural number is not an
#integer, then it is irrational. The decimal expansion of such square roots i
#infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880..., and the digital sum of
#the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums
#of the first one hundred decimal digits for all the irrational square roots.

# PNG:
# joder que mal explicado, no eran los primeros 100 dígitos, eran calculamos
# los primeros 100 dígitos MAS los dígitos enteros... ¬¬ en fin, que se
# explican como el puto CU-LO

#Find the square root of 2.
#          1. 4  1  4  2
#       /
#     \/  02.00 00 00 00

#         02                  1*1 <= 2 < 2*2                 x = 1
#         01                    y = x*x = 1*1 = 1
#         01 00               24*4 <= 100 < 25*5             x = 4
#         00 96                 y = (20+x)*x = 24*4 = 96
#            04 00            281*1 <= 400 < 282*2           x = 1
#            02 81              y = (280+x)*x = 281*1 = 281
#            01 19 00         2824*4 <= 11900 < 2825*5       x = 4
#            01 12 96           y = (2820+x)*x = 2824*4 = 11296
#               06 04 00      28282*2 <= 60400 < 28283*3     x = 2
#                             The desired precision is achieved:
#                             The square root of 2 is about 1.4142


def raiz_x(p, c):
    # x(20p+x) <= c
    x = 0
    while x*((20*p)+x) <= c:
        x += 1

    return x-1


def raiz_sum_dec(n, decimales):
    # pasamos el número a cadena, y añadimos un 0 delante si es impar el número
    # de dígitos
    if len(str(n)) % 2 == 0:
        num = str(n)
    else:
        num = '0' + str(n)

    c = 0
    p = 0
    numdec = 0
    sumdec = 0
    while numdec < decimales-1:

        # los dos dígitos a tratar
        if len(num) > 0:
            c = (c*100) + int(num[0:2])
            num = num[2:]
        else:
            if c == 0 and numdec == 0:
                return 0
            c = c * 100
            numdec += 1

        x = raiz_x(p, c)
        y = ((20*p)+x)*x
        p = (p*10)+x

        # el nuevo c...
        c = c - y

        sumdec += x

    return sumdec


def result():
    sumatory = 0
    for r in range(1, 101):
        sumatory += raiz_sum_dec(r, 100)

    # print("Resultado 0080:", sumatory)
    return sumatory
