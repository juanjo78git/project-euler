#! /usr/bin/python2

import itertools, math
N = 1000
nsol = [0]*N
for a in xrange(1, N-N/2):
	for b in itertools.count(a+1):
        	c_squared = a*a + b*b
        	c = int( math.sqrt( c_squared))
        	p = a + b + c
        	if not p < N: break
        	if c*c == c_squared:
			nsol[p] += 1
print nsol.index( max( nsol))
