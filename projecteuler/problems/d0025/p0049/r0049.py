# -*- coding: utf-8 -*-

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
#increases by 3330, is unusual in two ways:
    #(i) each of the three terms are prime, and,
    #(ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
#exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this
#sequence?


def isprime(n):
    if n == 1:
        return False

    # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def lista_primos_ddigits(d):
    """ un listado de números primos con d digitos """
    lprimos = []
    j = 2

    while True:
        if isprime(j):

            if len(str(j)) == d:
                lprimos.append(j)
            elif len(str(j)) > d:
                return lprimos
        j = j + 1


def result():

    maxvalue = 0

    lprimos = lista_primos_ddigits(4)

    # print(lprimos, len(lprimos))

    for i in range(0, len(lprimos)):
        for j in range(i+1, len(lprimos)):

            # incrementa en ... (claridad)
            incr = lprimos[j] - lprimos[i]
            tercer = lprimos[j] + incr

            if tercer in lprimos:

                isort = "".join(sorted(str(lprimos[i])))
                jsort = "".join(sorted(str(lprimos[j])))
                ksort = "".join(sorted(str(tercer)))

                if isort == jsort == ksort:
                    n = int('{}{}{}'.format(lprimos[i], lprimos[j], tercer))
                    if n > maxvalue:
                        maxvalue = n
                    # print lprimos[i], lprimos[j], tercer

    return maxvalue
