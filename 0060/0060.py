#!/usr/bin/pypy

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
#and concatenating them in any order the result will always be prime. For 
#example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
#primes, 792, represents the lowest sum for a set of four primes with this
#property.

#Find the lowest sum for a set of five primes for which any two primes 
#concatenate to produce another prime.

#lprimes= [2,23,41,73,87]
#list(itertools.combinations(lprimes, 2))

#luego con esta lista solo tengo que ir cogiendo cada uno de los elementos
#y ver que tanto en un orden como en otro es un primo...

import itertools

# es un número primo
def isprime(n):
	if n == 1:
		return False
	# rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True


# una lista de n primos


def lprimos(n):
	numprimos = 0
	nprime = 2
	lprime = []
	while len(lprime) != n:
		if isprime(nprime):
			lprime.append(nprime)
		nprime = nprime + 1	
	return lprime
	

def concatprimes(lcomb):
	p1 = lcomb[0]
	p2 = lcomb[1]
	p12 = int(str(p1) + str(p2))
	p21 = int(str(p2) + str(p1))
	
	if isprime(p12) and isprime(p21):
		return True
	else:
		return False

def compcombinac(lxprimes):
	llcomb = list(itertools.combinations(lxprimes, 2))

	for lcomb in llcomb:
		if not concatprimes(lcomb):
			return False

	return True


nprimos = 1000
lprime = lprimos(nprimos)

for pi1 in range(0, nprimos-4):
	
	p1 = lprime[pi1]
	
	for pi2 in range(pi1+1, nprimos-3):
	
		l2primes = []
		p2 = lprime[pi2]
		
		l2primes.append(p1)
		l2primes.append(p2)

		if not compcombinac(l2primes):
			continue

		for pi3 in range(pi2+1, nprimos-2):
			
			l3primes = []
			p3 = lprime[pi3]
		
			l3primes.append(p1)
			l3primes.append(p2)
			l3primes.append(p3)

			if not compcombinac(l3primes):
				continue

			
			for pi4 in range(pi3+1, nprimos-1):
	
				l4primes = []
				p4 = lprime[pi4]
		
				l4primes.append(p1)
				l4primes.append(p2)
				l4primes.append(p3)
				l4primes.append(p4)	
				
				if not compcombinac(l4primes):
					continue
						
				for pi5 in range(pi4+1, nprimos): 
					p5 = lprime[pi5]
					
					l5primes = []
					
					l5primes.append(p1)
					l5primes.append(p2)
					l5primes.append(p3)
					l5primes.append(p4)
					l5primes.append(p5)
				
					if compcombinac(l5primes):
						print("Resultado 0060:", sum(l5primes))
						exit(0)
						
						
				
				
				
				
				
				
				
				
		 