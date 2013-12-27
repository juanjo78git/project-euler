#!/usr/bin/python
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
            # print n, x, int(y)
        x += 1
    return total


LIMITE = 1000
n = 4
while True:
    t = calc_n(n)
    if n % 10000 == 0:
        print n, t

    if t > 1000:
        break
    n += 1

print "Resultado 0108: ", n
