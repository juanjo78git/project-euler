#! /usr/bin/python2

# esta solucion es superfea pedro

# vamos a crear una lista que contendra todos los valores

n20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen","fourteen","fifteen","sexteen","seventeen", "eighteen", "nineteen"]
n10s = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
n100s = ["hundred"]
n1000s = ["thousand"]

numeros = []


def n4s(n):
	s = ""
	for i in range(0, (4 - len(str(n)))):
		s = s + "0"
	
	return (s + str(n))
		

def cientos(n):
	
	s = n4s(n)
	
	digito = int(s[1])
	
	if (digito > 0):
		salida = n20[digito] + " " + n100s[0]
		
		if (n % 100):
			return salida + " and "
		else:
			return salida
	
	return ""


def decenas(n):

	s = n4s(n)
	digito = int(s[2])
	
	if (int(s[2]) < 2):
		salida = n20[int(s[2:4])]
	else:
		salida = n10s[digito] + " " +n20[int(s[3])]

	return salida


def miles(n):
	s = n4s(n)
	
	digito = int(s[0])
	
	if (digito > 0):
		salida = n20[digito] + " " + n1000s[0]
		
		if (n % 1000):
			return salida + " and "
		else:
			return salida
	
	return ""

suma = 0
for n in range(1, 1001):

	c = cientos(n)
	d = decenas(n)
	m = miles(n)

	suma = suma + len((m + c + d).replace(" ", "")) 

print suma


