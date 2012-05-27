#!/usr/bin/pypy

def is_square(n):
	square = n**0.5
	if int(square) == square:
		return True
	else:
		return False


def diophantine(d, x):	
	dv, md = divmod((x**2)-1, d)
	if md == 0:
		y = dv**0.5
		if int(y) == y:
			return True
	return False


D_result = 0
x_min = -1
limite = 1000
#limite = 13
for D in range(1, limite+1):
	print(D)
	x = 2
	if not is_square(D):
		while not diophantine(D, x):
			x += 1
		
		if x > x_min:
			x_min = x
			D_result = D

print(D_result, x_min)

