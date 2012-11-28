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

# es un número primo

def mcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def is_resilient(n, d):
    if (n == 1):
        return True
   
    # si ambos pares, fuera
    if (n % 2 == 0) and ((d - 1) % 2 == 0):
        return False


    if mcd(n, d - 1) == 1:
        return True
    else:
        return False

# el número de resilient, y el total, que será siempre d-1
def is_0243(nresi, d):
    if (nresi < 1):
        return False

    if (d < 2):
        return False

    if (nresi / (float)(d - 1)) < 0.1635881955585578:
        return True
    else:
        return False



nresi = 1
d = 725000

while (True):
    nresi = 0
    for numerator in range(1, d):
        if (is_resilient(numerator, d)):
            nresi = nresi + 1

    # trazas
    # print("resultados para", d, nresi)

    if (is_0243(nresi, d)):
        break

    # avanzamos al siguiente
    d = d + 1

    if (d % 1000 == 0):
        print("d:", d)

# si salimos es que tenemos solucion...
print("Resultado 0243:", d)



