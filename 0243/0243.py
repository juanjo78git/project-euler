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
            n = n // i
    
        if (n == 1):
            return ldiv

def is_resilient(ldivs, n, d):
    if n == 1:
        return True
    
    if ldivs[n] == None or ldivs[d] == None:
        return False
    
    for ni in ldivs[n]:
        if ni in ldivs[d]:
            return False

    return True

# el número de resilient, y el total, que será siempre d-1
def is_0243(nresi, d):
    #print("is_0253", nresi, d)


    if (nresi < 1):
        return False

    if (d < 2):
        return False

    if (nresi / (d - 1)) < 0.1635881955585578:
        return True
    else:
        return False


    #dsol, msol = divmod(15499, 94744)
    #dresi, mresi = divmod(nresi, d - 1)

    #if (dresi < dsol):
        #return True
    #elif (dresi == dsol):
        #if (mresi < msol):
            #return True
        #else:
            #return False
    #else:
        #return False

# lista de los divisores por numero
ldivs = []

nresi = 1
d = 1

ldivs.append(getlistdiv(0))

while (True):
        ldivs.append(getlistdiv(d))

        nresi = 0
        for numerator in range(1, d):
            if (is_resilient(ldivs, numerator, d)):
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


