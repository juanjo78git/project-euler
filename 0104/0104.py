#!/usr/bin/pypy


def fibonacci():
    """ Generador de la secuencia Fibonacci..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def pandigital(s):
	p = "123456789"

	if "".join(sorted(s)) == p:
		return True
	else:
		return False

def presufpan(n):
	# el mod es rápido, y solo pago la difision cuando lo vea necesario...
	suf = str(n % 1000000000)[-9:]

	if pandigital(suf):
		pre = str(n / 1000000000)[0:9]
		if pandigital(pre):
			return True
	return False
	

f = fibonacci()
i = 0
while not (presufpan(f.next())):
	i += 1


print("Resultado 0104:", i)

