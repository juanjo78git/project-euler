# -*- coding: utf-8 -*-

# In the following equation x, y, and n are positive integers.
#
# 1/x + 1/y = 1/n
#
# For n = 4 there are exactly three distinct solutions:
#
# What is the least value of n for which the number of distinct solutions
# exceeds one-thousand?
#
# NOTE: This problem is an easier version of problem 110; it is strongly
# advised that you solve this one first.

import copy

from projecteuler import mymaths

def multlist(l):
    t = 1
    for i in l:
        t = t * i

    return t

def catch_divs_to_n(primes, ndivs):
    # 120 55440 [2, 3, 5, 7, 11]

    l = copy.deepcopy(primes)

    # por motivos extraños, 1 es
    l.append(1)

    v = 2

    while mymaths.numdivs(multlist(l)) < ndivs:
        print('mult', multlist(l))
        print(v)
    # while calc_n(v) < ndivs:
        if v not in l:
            d = mymaths.lnumdivs(v)
            add = True
            for i in d:
                if i not in l:
                    add = False
                    break

            if add:
                print(v)
                l.append(v)
        v += 1

    print(mymaths.numdivs(multlist(l)))
    print(l)
    print(multlist(l))


def calc_a(n, m):
    """ esta función está mal de cojones """
    
    # y = m*n/m-1

    d = divmod(n * m, m - 1)
    # print(n, m, d)

    if d[1] == 0:
        return d[0]
    else:
        return None

def check(x, y, n):
    return (n * (x + y)) < (x * y)


def calc_n(n):
    total = 0
    x = n + 1
    while True:
        # si recien cambiadoya no cumple, fuera
        if (check(x, x, n)):
            break

        # calculamos la y
        y = (n * x * -1) / (float(n - x))
        if y == int(y):
            # es solución
            total += 1
            # print('n: {} --> 1/{} + 1/{} = 1/{}'.format(n, x, int(y), n))
        x += 1
    return total







def result():
    
    LIMITE = 1000

    # for n in range(180180, 180181):
    # for n in range(1, 20):
    #     print(calc_n(n))
   
    n = 0
    t = 0

    while True:
        n += 1
        print(n)
        t = calc_n(n)
        if t > LIMITE:
            return n
        

    # catch_divs_to_n([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 1000)
    # catch_divs_to_n([2, 3, 5, 7, 11], 1000)

    # LIMITE = 1000
    # n = 4
    # n = 518918400
    # n = 180180

    # r = 0

    # while True:
    # for m in range(2, n + 2):
    #     a = calc_a(n, m)
    #     # print(a)

    #     if a:
    #         if a == n:
    #             # print(r)
    #             print('r', r)
    #             return 0
    #         else:
    #             r += 1


    # print('r', r)
