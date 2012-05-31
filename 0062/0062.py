#!/usr/bin/python


# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 
# 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest
# cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are
# cube.




def dcube_add(dcubo, cubo):

	# nos quedamos con el cubo ordenado
	cubosort = "".join(sorted(str(cubo)))

	if cubosort in dcubo:
		dcubo[cubosort].append(cubo)
	else:
		lcubo = []
		lcubo.append(cubo)
		dcubo[cubosort] = lcubo

	return dcubo	

def dcube_busca_n(dcubo, n):
	for k in dcubo:
		if len(dcubo[k]) == n:
			print("Resultado:", dcubo[k][0])
			return True
	
	return False




salida = False
cubo = 0
icubo = 1
dcubo = {}
while not salida:
	cubo = icubo ** 3
	#print(cubo)
	icubo += 1	
	# se añade
	dcubo = dcube_add(dcubo, cubo)
	#print(dcubo)
	# deberíamos buscar alguno! con un total de n datos!!
	if dcube_busca_n(dcubo, 5):
		exit(0)
