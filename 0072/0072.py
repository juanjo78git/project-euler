#!/usr/bin/pypy

#Consider the fraction, n/d, where n and d are positive integers. If nd and 
#HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d  8 in ascending order 
#of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 
#5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that there are 21 elements in this set.

#How many elements would be contained in the set of reduced proper fractions 
#for d  1,000,000?

def mcd(a, b):
	if b == 0:
		return a
	else:
		return mcd(b, a % b)

def mcd_it(a, b):
	while b != 0:
		aux = b
		b = a % b
		a = aux
	return a
		
limite = 1000000
total = 0


# n/d
for d in range(1, limite+1):
	if d % 10000 == 0:
		print(d)
	for n in range(d+1, limite+1):
		if mcd_it(n, d) == 1:
			total += 1

print("Resultado 0072:", total)
