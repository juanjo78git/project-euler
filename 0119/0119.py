# -*- coding: utf-8 -*-

#!/usr/bin/pypy

from datetime import datetime

TH = 30
#L = 10000
#N = 10000

N = 100
E = 100

powers = []


def sumdigits(n):
    sumatory = 0
    for i in str(n):
        sumatory += int(i)
    return sumatory

def gen_pos_result(N, E):
    powers = []
    for i in range(2, N):
        for j in range(2, E):
            power = i ** j
            if sumdigits(power) == i:
                powers.append(power)
    return powers


# controlamos el tiempo de ejecución
start_time = datetime.now()

powers = gen_pos_result(N, E)
powers.sort()

print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0123: ", powers[TH - 1]
