#! /usr/bin/python2

def orden_int(n):
	letras = []
	for c in str(n):
		letras = [c] + letras

	letras.sort()
	
	return int("".join(letras))


def lista_iguales(li):
	e1 = li[0]
	
	for ex in li:
		if e1 != ex:
			return False
	
	return True

n = 0
while True:
	n = n + 1
	
	numeros = []
	for i in range(1, 7):
		numeros = numeros + [orden_int(n*i)]
	
	if lista_iguales(numeros):
		break

print numeros
print n

	
		


