#!/usr/bin/python

# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import os
import sys

from projecteuler import mymaths

def result():
    resultado = 0
    exit = False

    for a in range(1, 1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if a+b+c == 1000 and mymaths.ispythagoreantriplet(a, b, c):
                    resultado = a*b*c
                    exit = True
                    break
            if exit:
                break
        if exit:
            break

    return resultado
