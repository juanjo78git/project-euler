# -*- coding: utf-8 -*-

# Problem 111
#
# Considering 4-digit primes containing repeated digits it is clear that they
# cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and
# so on. But there are nine 4-digit primes containing three ones:
#
# 1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
#
# We shall say that M(n, d) represents the maximum number of repeated digits
# for an n-digit prime where d is the repeated digit, N(n, d) represents the
# number of such primes, and S(n, d) represents the sum of these primes.
#
# So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime
# where one is the repeated digit, there are N(4, 1) = 9 such primes, and the
# sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is
# only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13
# such cases.
#
# In the same way we obtain the following results for 4-digit primes.
#
# |Digit, d |   M(4, d) | N(4, d)       | S(4, d)
# | ------- | --------- | ------------- | -------
# |0        | 2         | 13            | 67061
# |1        | 3         | 9             | 22275
# |2        | 3         | 1             | 2221
# |3        | 3         | 12            | 46214
# |4        | 3         | 2             | 8888
# |5        | 3         | 1             | 5557
# |6        | 3         | 1             | 6661
# |7        | 3         | 9             | 57863
# |8        | 3         | 1             | 8887
# |9        | 3         | 7             | 48073
#
# For d = 0 to 9, the sum of all S(4, d) is 273700.
#
# Find the sum of all S(10, d).

import itertools

from projecteuler import mymaths


def M(n, d):
    """ Calcula el máximo número de repeticiones del número d de tamaño n """
    
    # Tratamos caso que ddd...d sea primo
    if mymaths.isprime(int(str(d) * n)):
        return n

    for i in range(1, n):
        # print('i', i)

        dx = str(d) * (n - i)
        # print('dx', dx)

        for j in range(0, 10 ** i):
            # print('j', j)

            v = ('0' * (i - len(str(j)))) + str(j)
            # print('v', v)

            dxv = dx + v
            # print('dxv', dxv)
            
            for p in list(set(itertools.permutations(dxv))):
                p1 = ''.join(p)

                # caso de 00..00X
                if len(str(int(p1))) != n:
                    continue

                if mymaths.isprime(int(p1)):
                    # print('p', p)
                    return n - i


def N_S(n, d):
    
    primes = []
    
    m = M(n, d)
    i = n - m
    # print('m i', m, i)

    # print('dx', dx)
    dx = str(d) * (n - i)

    for j in range(0, 10 ** i):
        # print('j', j)

        v = ('0' * (i - len(str(j)))) + str(j)
        # print('v', v)

        dxv = dx + v
        # print('dxv', dxv)
        
        for p in list(set(itertools.permutations(dxv))):
            p1 = int(''.join(p))

            # caso de 00..00X
            if len(str(p1)) != n:
                continue

            if mymaths.isprime(p1):
                # print(p1)
                # total += 1
                # summ += int(p1)
                if not p1 in primes:
                    primes.append(p1)

    return len(primes), sum(primes)


    

def result():

    d = 10
    t = 0
   
    for i in range(0, 10):
        v_N, v_S = N_S(d, i)
        # print(i, v_N, v_S)
        t += v_S
    
    
    return t
