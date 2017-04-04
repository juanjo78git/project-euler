# -*- coding: utf-8 -*-

# Consider the fraction, n/d, where n and d are positive integers. If nd
# and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d  8 in ascending order
# of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
# proper fractions for d  12,000?
# Note: The upper limit has been changed recently.


def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def mcd_it(a, b):
    while b != 0:
        aux = b
        b = a % b
        a = aux
    return a


def result():
    n_fix_inf = 1
    d_fix_inf = 3

    n_fix_sup = 1
    d_fix_sup = 2

    total = 0

    limite = 12000

    # n/d
    for d in range(1, limite+1):

        # limite inferior a la primera facción
        n_inf, m = divmod(n_fix_inf*d, d_fix_inf)
        n_sup, m = divmod(n_fix_sup*d, d_fix_sup)

        for n in range(n_inf-1, n_sup+2):

            if mcd_it(n, d) == 1:
                cond1 = (n*d_fix_inf) > (d*n_fix_inf)
                cond2 = (n*d_fix_sup) < (d*n_fix_sup)
                if cond1 and cond2:
                    # print(n,d)
                    total += 1

    # print("Resultado 0073:", total)
    return total
