# -*- coding: utf-8 -*-

#It is possible to show that the square root of two can be expressed as an
#infinite continued fraction.

#RAIZ_CUADRADA 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

#By expanding this for the first four iterations, we get:

#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

#The next three expansions are 99/70, 239/169, and 577/408, but the eighth
#expansion, 1393/985, is the first example where the number of digits in the
#numerator exceeds the number of digits in the denominator.

#In the first one-thousand expansions, how many fractions contain a numerator
#with more digits than denominator?


def next_numerator_denominator(n, d):
    nnext = (2*d)+n
    dnext = n+d
    return nnext, dnext


def result():
    n_iteraciones = 1000
    numerator_more_digits = 0
    n = 3
    d = 2

    for i in range(0, n_iteraciones):
        if len(str(n)) > len(str(d)):
            numerator_more_digits = numerator_more_digits + 1

        n, d = next_numerator_denominator(n, d)

    return numerator_more_digits
