#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
from operator import mul

lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

# import mymaths


def get_k(nums):
    """ a partir de una lista de números nos devuelve el valor de k """
    sumatory = sum(nums)
    product = reduce(mul, nums, 1)

    k = len(nums) + ((product - sumatory))
    # return len(nums) + ((product - sumatory))
    # print "k: ", k, " -- valor sumatorio: ", product, "lista: ", nums
    return k


def res(k_max, limit):
    result = {}
    for n in range(4, limit):

        # tenemos que ir sacando todos los posibles divisores de n
        if n % 1000 == 0:
            print n
        m = n
        for d1 in range(2, ((n / 2) + 1)):
            divs = []
            m = n
            for d2 in range(d1, ((n / 2) + 1)):
                while m % d2 == 0:
                    m = m / d2
                    if m > 1:
                        # tenemos un divisor
                        divs.append(d2)
                        k = get_k(divs + [m])
                        
                        if k < k_max + 1:

                            if result.has_key(k):
                                if result[k] > n:
                                    result[k] = n
                            else:
                                result[k] = n

    s = sum(list(set(result.values())))
    print s
    return s


# controlamor el tiempo de ejecución
start_time = datetime.now()

# s1 = res(12, 100)
s2 = res(12000, 100000)

print cadena_maxima
print "Tiempo total: ", datetime.now() - start_time
print "Resultado de 0088: s2", 
