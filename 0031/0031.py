#! /usr/bin/python

#In England the currency is made up of pound, £, and pence, p, and there are 
#eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:

#1£1 + 150p + 220p + 15p + 12p + 31p
#How many different ways can £2 be made using any number of coins?




total = 0

for p1 in range (0, 200+1):
	tsum = p1 * 1
	if tsum > 200:
		break
	for p2 in range (0, 100+1):
		tsum = (p2 * 2) + (p1 * 1)
		if tsum > 200:
			break		
		for p5 in range (0, 40+1):
			tsum = (p5 * 5) + (p2 * 2) + (p1 * 1)
			if tsum > 200:
				break
			for p10 in range (0, 20+1):
				tsum = (p10 * 10) + (p5 * 5) + (p2 * 2) + (p1 * 1)
				if tsum > 200:
					break
				for p20 in range (0, 10+1):
					tsum = (p20 * 20) + (p10 * 10) + (p5 * 5) + (p2 * 2) + (p1 * 1)
					if tsum > 200:
						break
					for p50 in range (0, 4+1):
						tsum = (p50 * 50) + (p20 * 20) + (p10 * 10) + (p5 * 5) + (p2 * 2) + (p1 * 1)
						if tsum > 200:
							break
						for l1 in range (0, 2+1):
							tsum = (l1 * 100) + (p50 * 50) + (p20 * 20) + (p10 * 10) + (p5 * 5) + (p2 * 2) + (p1 * 1)
							if tsum > 200:
								break
							for l2 in range (0, 1+1):
								tsum = (l2 * 200) + (l1 * 100) + (p50 * 50) + (p20 * 20) + (p10 * 10) + (p5 * 5) + (p2 * 2) + (p1 * 1)
								if tsum > 200:
									break
							
								if tsum == 200:
									total = total + 1


print("Diferentes maneras:", total)




