#!/usr/bin/python


def babylonian(s, x):
	return (0.5*(x + s/x))

s = 2
x = 4
for i in range(1, 100000):
	x = babylonian(s, x)

print(x)

