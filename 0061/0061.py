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

# joder, le paso la función como parámetro y listo, la uso como fn(n)
def lxnal(fn):
	l = []
	n = 1
	slen = 0
	while slen < 5:
		t = fn(n)
		slen = len(str(t))	
		if slen == 4:
			l.append(t)
		n += 1
	return l	

# prefijo serían ya los dos dos primeros números
def tiene_prefijo(pre, l):
	for x in l:
		if pre == str(x)[0:2]:
			return True
	return False
	
def tiene_sufijo(suf, l):
	for i in l:
		if suf == str(i)[2:4]:
			return True
	return False

def busca_pre_suf(n, l):
	#print(n, i, l)
	
	pre = str(n)[0:2]
	suf = str(n)[2:4]
	bpre = False
	bsuf = False
	
	for lx in l:
		if tiene_prefijo(pre, lx):
			bpre = True
		
		if tiene_sufijo(suf, lx):
			bsuf = True

	return bpre and bsuf


np = 6		 
l = []

# increiblemente facil
l.append(lxnal(triangle))
l.append(lxnal(square))
l.append(lxnal(pentagonal))
l.append(lxnal(hexagonal))
l.append(lxnal(heptagonal))
l.append(lxnal(octagonal))

for lx in l:
	print(len(lx))
	#print(lx)



li = 0
lcopy = list(l)
print(id(lcopy), id(l))
for lx in l:
	lminus = list(l)	
	lminus.pop(li)
	for i in lx:
		if not busca_pre_suf(i, lminus):
			lcopy[li].remove(i)
			
	li += 1	
		

for lx in lcopy:
	print(len(lx))
	#print(lx)	

