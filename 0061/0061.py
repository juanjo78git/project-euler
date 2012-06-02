#!/usr/bin/python

def triangle(n):
	return int(n*(n+1)/2)

def square(n):
	return int(n**2)

def pentagonal(n):
	return int(n*(3*n-1)/2)

def hexagonal(n):
	return int(n*(2*n-1))

def heptagonal(n):
	return int(n*(5*n-3)/2)

def octagonal(n):
	return int(n*(3*n-2))



for n in range(1, 10):
	print(triangle(n))


