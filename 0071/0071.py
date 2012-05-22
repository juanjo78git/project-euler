#!/usr/bin/pypy

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
		
		
d_fix = 7
n_fix = 3
d_ant = 1000000
n_ant = 1
limite = 1000000

# n/d
for d in range(limite, 1, -1):

	if d % 1000 == 0:
		print("d", d)

	for n in range(1, d):
		if n % 100000 == 0:
			print("n y d",n, d)
			
		# una vez es mayor, debemos romper
		if (n*7) > (d*3):
			break
		
		if mcd_it(n, d):
			# quiero ver si el número es menor que 3/7...
			if (n*7) < (d*3):
				if (n*d_ant) > (d*n_ant):
					d_ant = d
					n_ant = n
print(d, n)