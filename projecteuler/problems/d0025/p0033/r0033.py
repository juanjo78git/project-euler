#!/usr/bin/python2


def divisores_euclides(n):
    divisores = []
    for i in range(2, n/2+1):
        print i
        while n % i == 0:
            print "ok"
            n = n / i
            divisores.append(i)

    return divisores

print divisores_euclides(49)
