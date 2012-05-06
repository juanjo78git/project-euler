#! /usr/bin/python

def isprime(n):
	if n == 1:
		return False
	
	# range starts with 2 and only needs to go up the squareroot of n
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True

# solo queremos que el último primo sea mayor que N, así saldrán
# menos números
def lista_primos(n):
	num = 2
	lprimos = []
	while num < n:
		if isprime(num):
			lprimos.append(num)
		num += 1
	return lprimos

N = 1000000
maxprime = 0
lprime = lista_primos(N)
maxelem = 0

print(lprime)
print(len(lprime))

for i in range(0, len(lprime)):
	j = i+1
	suma = sum(lprime[i:j])
	
	while suma < N and len(lprime) > j:
		if isprime(suma):
			if (j - i) > maxelem:
				maxprime = suma
				maxelem = j - 1
				print("primo:", suma, lprime[i:j], i, j) 
				
		j += 1
		suma = sum(lprime[i:j])

print(maxprime)

			
			
		 
