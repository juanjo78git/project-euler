def lista_factores(n):
	lifactores = []
	div = 2
	factor = -1
	while (1):
		if (n % div) == 0:
			if (factor == -1):
				factor = div
			else:
				factor *= div
			
			n /= div
		else:
			div += 1
			
			if (factor != -1):
				lifactores.append(factor)
			
			factor = -1
			
			if n == 1:
				break
			
	return lifactores
	
def factores_todos_distintos(lista_a, lista_b):
	for a in lista_a:
		for b in lista_b:
			if a == b:
				return False
	return True
	
def f_47(l1, l2, l3, l4):
	if (len(l1) != 4) or (len(l2) != 4) or (len(l3) != 4) or (len(l4) != 4):
		return False
	
	if not factores_todos_distintos(l1, l2):
		return False

	if not factores_todos_distintos(l1, l3):
		return False
	
	if not factores_todos_distintos(l1, l4):
		return False
	
	if not factores_todos_distintos(l2, l3):
		return False
	
	if not factores_todos_distintos(l2, l4):
		return False
	
	if not factores_todos_distintos(l3, l4):
		return False
	
	return True
	

	
#programa principal
if True:
	l1 = [1]
	l2 = [1]
	l3 = [1]
	l4 = [1]
	exit = False
	n = 2

while not exit:
	
	l1 = l2
	l2 = l3
	l3 = l4
	l4 = lista_factores(n + 3)
	
	exit = f_47(l1, l2, l3, l4)
	
	if exit:
		print "resultado", n
	
	print n
	n += 1
	
	


