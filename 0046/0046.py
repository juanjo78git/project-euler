#!/usr/bin/python

# It was proposed by Christian Goldbach that every odd composite number can be 
# written as the sum of a prime and twice a square.
# 
# 9 = 7 + 212
# 15 = 7 + 222
# 21 = 3 + 232
# 25 = 7 + 232
# 27 = 19 + 222
# 33 = 31 + 212
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime 
# and twice a square?

# idea:
#
# listade primos = dame lista de primos
#
# for n in range(impares):
#	if n es primo:
#		break
#	
#	buscamos en nuestra lista de primos el primer elemento i mayor que n
#	for (0 to elemento i que sabemos que es el primo mayor que n):
#		for j in range(1 .. raizcuadrada(n/2) +1
#			
#			if (n == listadeprimos[i] + 2*j^2):	
#				print(n)
#				exit(0)
# solucionado! a falta de picar (eso espero!)
# los tiempos serán buenos... el único problema es delimitar cuandos primos
# guardamos, aunque una chapuza sería para cada bucle generar un listado
# de primos menos que n... me-nu-da chapuza... --> quizás mejor sería que
# el bucle del medio estuviera el último, que es el más pesado por el tema
# de los primos... <-- gran idea