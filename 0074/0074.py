#!/usr/bin/pypy

#The number 145 is well known for the property that the sum of the factorial of
#its digits is equal to 145:

#1! + 4! + 5! = 1 + 24 + 120 = 145

#Perhaps less well known is 169, in that it produces the longest chain of
#numbers that link back to 169; it turns out that there are only three such
#loops that exist:

#169  363601  1454  169
#871  45361  871
#872  45362  872

#It is not difficult to prove that EVERY starting number will eventually get
#stuck in a loop. For example,

#69  363600  1454  169  363601 ( 1454)
#78  45360  871  45361 ( 871)
#540  145 ( 145)

#Starting with 69 produces a chain of five non-repeating terms, but the longest
#non-repeating chain with a starting number below one million is sixty terms.

#How many chains, with a starting number below one million, contain exactly
#sixty non-repeating terms?

# Funcion para el factorial

fact10 = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def fact_under_10(x):
    global fact10
    return fact10[x]


def sumfactorial(n):
    suma = 0
    for c in str(n):
        suma += factorial(int(c))
    return suma


def ciclossumfactorial(n):
    ciclos = 0
    lnext = []
    next = n
    while next not in lnext:
        ciclos += 1
        lnext.append(next)
        next = sumfactorial(next)
    return ciclos


limite = 1000000
total = 0

for n in range(1, limite):
#    if n % 1000 == 0:
#        print(n)
    if ciclossumfactorial(n) == 60:
        total += 1

print("Resultado 0074:", total)
