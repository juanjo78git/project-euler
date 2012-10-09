#!/usr/bin/python3

# A positive fraction whose numerator is less than its denominator is called 
# a proper fraction.
# 
# For any denominator, d, there will be d1 proper fractions; for example, 
# with d = 12
# 1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.
#
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be 
# the ratio of its proper fractions that are resilient; for example, 
# R(12) = 4/11 .
# In fact, d=12 is the smallest denominator having a resilience R(d) < 4/10 .
#
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

# necesitaremos una variable global para guardar todos los divisores
# de cada uno de los numeros....

def getlistdiv(n):
    ldiv = []
    for i in range(2, n + 1):
        if (n % i == 0):
            ldiv.append(i)

        # solo queremos una lista de primos, no de divisores
        while (n % i == 0 and n != 1):
            n = n / i
    
        if (n == 1):
            return ldiv

def is_resilient(ldivs, n, d):
    for ni in ldivs[n]:
        if ni in ldivs[d]:
            return False

    return True



ldivs = []

for i in range(0,10):
    ldivs.append(getlistdiv(i))


print(is_resilient(ldivs, 4, 9))
