def mcd(a, b):
	if b == 0:
		return a
	else:
		return mcd(b, a % b)
		

class Pe71(object):
	def __init__(self, valor=1, dividendo=1, divisor=1):
		self.valor = valor
		self.dividenco = dividendo
		self.divisor = divisor

lista_ope71 = []
for d in range(1, 100):
	for n in range(1, d):
		if mcd(n, d) == 1:
			
			if (n/float(d) <= 3/float(7):
				ope71 = Pe71(n/float(d), n, d)
				lista_ope71.append(ope71)