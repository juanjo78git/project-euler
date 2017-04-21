# -*- coding: utf-8 -*-

from projecteuler import mymaths

R = 0

def _sum_digits_int(n):
    t = 0
    for c in str(n):
        t += int(c)

    return t

def h(n, maxlen):

    # testeamos si n es H
    len_n = len(str(n))

    if len_n < maxlen:
        if mymaths.isprime(n) and len(str(n)) > 1:
            # print('n', n)
            m = int(str(n)[:-1])
            # print('m', m)
            d = divmod(m, _sum_digits_int(m))
            # print('d', d)
            if mymaths.isprime(d[0]):
                # print(n)
                global R
                R += n
                return

        d = divmod(n, _sum_digits_int(n))

        if d[1] != 0:
            return
        
        # if not mymaths.isprime(d[0]):
        #     return

        for i in range(0, 10):
            new_n = int(str(n) + str(i))
            h(new_n, maxlen)
    else:
        return


def result():
    global R
    R = 0

    LIMITE = 15

    print('1')
    h(1, LIMITE)
    print('2')
    h(2, LIMITE)
    print('3')
    h(3, LIMITE)
    print('4')
    h(4, LIMITE)
    print('5')
    h(5, LIMITE)
    print('6')
    h(6, LIMITE)
    print('7')
    h(7, LIMITE)
    print('8')
    h(8, LIMITE)
    print('9')
    h(9, LIMITE)

    return R
