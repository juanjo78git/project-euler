#! /usr/bin/python

def pandigital9(m1, m2, r):
	s = str(m1) + str(m2) + str(r)
	
	if len(s) != 9:
		return False
	
	for i in range(1, 10):
		if s.find(str(i)) == -1:
			return False
	
	return True



b = pandigital9(9233,456,781)
print(b)
