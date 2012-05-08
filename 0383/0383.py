#!/usr/bin/python

# @TODO esto escapa a mi comprensión, con 10**4 ya es un suplicio, cuando
# sea mayor lo intentaré


import math

def f5(n):
	x = 0
	while True:
		n, m = divmod(n, 5)

		if m != 0:
			return x
		
		x = x + 1	 


#print(math.factorial(30000))

#print(f5(625000))

n = 10**4
total = 0

for i in range(1, n+1):
	
	a = math.factorial((2*i)-1)
	b = math.factorial(i)
	
	if f5(a) < 2*f5(b):
		total = total + 1
		
print(total)
