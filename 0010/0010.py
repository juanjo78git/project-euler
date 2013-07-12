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
lib_path = os.path.abspath('../lib')
sys.path.append(lib_path)

import mymaths

p = mymaths.prime()
limite = 2000000
sumprimos = 0
primo = 0
while (primo < limite):
    sumprimos += primo
    primo = p.next()

print ("Resultado 0010", sumprimos)
