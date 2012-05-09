#!/usr/bin/pypy

# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.

# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

################################################################################




import random, sys

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
	
    for repeat in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True



























# es un número primo
def isprime(n):
	if n == 1:
		return False

	# rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False

	return True


	
def isnumdivprimes(n):

	

	# tratamientos previos
	# 1. un número impar nunca cumplirá, ya que siempre tendremos que el
	#	número tendría a si mismo como divisor, luego:
	#	n + (n / n) --> n/n sería 1, luego el número sería PAR
	#if n % 2 == 1:
	#	return False
	lastdigit = int(str(n)[len(str(n))-1])
	if lastdigit % 2 == 1:
	#if n  % 2 == 0:
		return False
	
	# 2. Similar al anterior, si termina en 4 o en 9 sería divisible entre 5
	if lastdigit == 4 or lastdigit == 9:
	#if n % 4 == 0 or n % 9 == 0:
		return False
	
	
	# 3. Los números que sumen sus dígitos 8 les pasará lo mismo, el n/n les
	# 	sumará 1 y se convertirán en divisibles por 3
	#if isdiv3(n + 1):
	if (n + 1) % 3 == 0:
		return False
		
	# En otro caso... lo hacemos a fuerza bruta, si vemos que es demasiado
	# buscaremos más trucos como los anteriores

	for d in range(1, n + 1):
		di,m = divmod(n, d)                
		if m == 0:
			p = d + di
			
			#if miller_rabin(p) != isprime(p):
			#	print p
			#	exit(0)
			
			
			#if not isprime(p):
			if not miller_rabin(p):
				return False	

	return True


#print(isnumdivprimes(30))
#sys.exit(0)

rango = 100000000
#rango = 1000000
total = 0

for n in range(1, rango + 1):

	if n % 10000 == 0:
		print (100*n)/float(rango)
	
	if isnumdivprimes(n):
		total = total + n

#print("Resultado para 0357:", total)
print total	




