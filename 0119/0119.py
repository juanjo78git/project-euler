# -*- coding: utf-8 -*-

#!/usr/bin/pypy

from datetime import datetime

TH = 30
L = 10000
N = 10000

powers = []


def sumdigits(n):
    sumatory = 0
    for i in str(n):
        sumatory += int(i)
    return sumatory


def is_0119(n):
    s = sumdigits(n)
    if s == 1:
        return False
    exp = 1

    # para ganar velocidad, vamos a ir dando saltos con el exponente hasta
    # dar con un número que sea mayor, luego restaremos este valor y así
    # saltamos muchos

    #while True:
        #exp += 2
        #power = s ** exp
        #if power > n:
            #exp -= 2
            #break

    while True:
        pos_power = powers[s][exp]
        if pos_power is None:
            power = s ** exp
            powers[s][exp] = power
        else:
            power = pos_power

        if power == n:
            print "%d = %d^%d" % (n, s, exp)
            return True
        elif power > n:
            return False
        exp += 1


def gen_default_powers(L, N):
    powers = range(0, L)
    for i in range(0, L):
        powers[i] = [None] * N
    return powers


# controlamos el tiempo de ejecución
start_time = datetime.now()

powers = gen_default_powers(L, N)

n = 10
i = 0
while True:
    if is_0119(n):
        i += 1
        print i
        if i == TH:
            break
    n += 1

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0123 ", n
