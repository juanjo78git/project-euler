#!/usr/bin/pypy



# es un número primo
def isprime(n):
        if n == 1:
                return False

        # rango empieza en 2, y solo tenemos que llegar hasta el cuadrado de n
        for x in range(2, int(n**0.5)+1):
                if n % x == 0:
                        return False
        return True

# lista de divisores
def divisors(n):
	ldivs = []
	
	for d in range(1, n + 1):
		if n % d == 0:
			ldivs.append(d)
	return ldivs




# es divisible por 3
def isdiv3(n):
	s = str(n)
	while len(s) > 1:
		n = 0
		for i in range(0, len(s)):
			n = n + int(s[i])
		s = str(n)
	
	if (int(s) == 3) or (int(s) == 6) or (int(s) == 9):
		return True
	else:
		return False
	
	
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
			if not isprime(int(p)):
				return False	

	return True


#print(isnumdivprimes(30))
#sys.exit(0)

rango = 100000000
#rango = 50000
total = 0

for n in range(1, rango + 1):

	if n % 10000 == 0:
		print (100*n)/float(rango)
	
	if isnumdivprimes(n):
		total = total + n

#print("Resultado para 0357:", total)
print total	




