#! /usr/bin/python2

import itertools

def isprime(n):
	if n == 1:
		return False
	
	# range starts with 2 and only needs to go up the squareroot of n
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True

for i in itertools.permutations('7654321'):
	x = int("".join(i))

	if isprime(x):
		print x
		break

