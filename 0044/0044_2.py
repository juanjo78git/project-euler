#!/usr/bin/python

#Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten 
#pentagonal numbers are:

#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 
#70  22 = 48, is not pentagonal.

#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
#difference is pentagonal and D = |Pk-Pj| is minimised; what is the value of D?


def pentagonal(n):
	return int((n*((3*n)-1)/2))


def ispentagonaldouble(i, j, k, h):
	pi = pentagonal(i)
	pj = pentagonal(j)
	pk = pentagonal(k)
	ph = pentagonal(h)
	
	if ((pj + pk) == ph) and ((pk-pj) == pi):
		print(pi, pj, pk, ph)
		return True
	else:
		return False


x = 10000

for i in range (1, x):
	for j in range(i, x):
		for k in range(i, x):
			for h in range(k, x):
				if ispentagonaldouble(i, j, k, h):
					print(pentagonal(k)-pentagonal(j))


