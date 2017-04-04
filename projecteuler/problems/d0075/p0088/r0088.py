# -*- coding: utf-8 -*-

from operator import mul


def get_k(nums):
    """ a partir de una lista de números nos devuelve el valor de k """
    sumatory = sum(nums)
    product = reduce(mul, nums, 1)

    k = len(nums) + ((product - sumatory))
    # return len(nums) + ((product - sumatory))
    # print "k: ", k, " -- valor sumatorio: ", product, "lista: ", nums
    return k


# http://stackoverflow.com/questions/24723721/
#      how-can-i-generate-all-possible-divisor-products-for-a-number 
def products(n, min_divisor=2):
    """Generate expressions of n as a product of ints >= min_divisor."""
    if n == 1:
        yield []
    for divisor in range(min_divisor, n+1):
        if n % divisor == 0:
            for product in products(n // divisor, divisor):
                yield product + [divisor]


def res(k_max):
    result = {}
    for n in range(4, (k_max * 2) + 1):

        # tenemos que ir sacando todos los posibles divisores de n
        # if n % 1000 == 0:
        # s = sum(list(set(result.values())))
        # print n, len(result.keys()), s
        for product in products(n):
            k = get_k(product)
            if k < k_max + 1:
                if result.has_key(k):
                    if result[k] > n:
                        result[k] = n
                else:
                    result[k] = n
    
    s = sum(list(set(result.values())))
    # print sorted(result.items(), key=lambda x: x[1])
    # print result
    
    # for i in sorted(result.keys()):
    #     print i, ":", result[i]
    # print s
    return s


def result():

    s2 = res(12000)

    # print "Resultado de 0088: ", s2
    return s2
