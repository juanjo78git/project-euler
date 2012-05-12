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


cumple = False

# empezamos en lado 5
lado = 5
nprimos = 0
sumatorio = 2
d = 1

while not cumple:
	
	# añadimos 4 elementos más
	for i in range(0,4):

		if isprime(d):
			nprimos = nprimos + 1
		
		d = d + sumatorio


	sumatorio = sumatorio + 2
	lado = lado + 2

	#print(nprimos, (lado*2)-1, (100*nprimos)/float((lado*2)-1))
	
	if ((100*nprimos)/float((lado*2)-1)) < 10:
		print("Solucion 0058:", lado)
		cumple = True

	
