 
 # implement a structure similar to C struct or Pascal record using a class
 
 # tested with Python24 vegaseat 11aug2005
 
  
 
 class Employee(object):
 
 def __init__(self, name=None, dept=None, salary=2000):
 
 self.name = name
 
 self.dept = dept
 
 self.salary = salary
 
class Pe71(objet):
	def __init__(self, valor=1, dividendo=1, divisor=1):
		self.valor = valor
		self.dividenco = dividendo
		self.divisor = divisor
  
 
 # one way to load the structure
 
 john = Employee('John Johnson', 'software', 3000)
 
 allan = Employee('Allan Armpit', 'hardware', 3400)
 
 mark = Employee('Mark Marksman', 'shipping/handling', 2600)
 
 zoe = Employee('Zoe Zoeller', 'wordprocessing', 2100)
 
  
 
 # another way to load the structure
 
 ted = Employee()
 
 ted.name = 'Ted Tetris'
 
 ted.dept = 'human resources'
 
 ted.salary = 5000
 
  
 
 # this works like a structure/record
 
 print "%s works in %s and earns $%s/month" % (zoe.name, zoe.dept, zoe.salary)
 
 print "%s works in %s and earns $%s/month" % (ted.name, ted.dept, ted.salary)
 
  
 
 print '-'*60
 
  
 
 # for a long list of employees you can do this
 
 empList = [allan, john, mark, ted, zoe]
 
 for emp in empList:
 
 print "%s works in %s and earns $%s/month" % \
 
 (emp.name, emp.dept, emp.salary)
 
  
 
 print '-'*60
 
  
 
 # ted had a sex change operation!
 
 ted.name = "Tanya Tetris"
 
 ted.salary = 4500
 
 print "%s works in %s and earns $%s/month" % (ted.name, ted.dept, ted.salary)
 
  
 
 print '-'*60
 
  
 
 # use list comprehension to get the average salary
 
 print "The average monthly salary of all employees: ",
 
 average_salary = sum([emp.salary for emp in empList])/len(empList)
 
 print "$%0.2f" % average_salary
 
 -----------------------------------------------------------
 >>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> print a
[1, 2, 3, 4, 5]

Sort takes an optional function which can be called for doing the comparisons. The default sort routine is equivalent to using cmp:

>>> print sorted([5, 2, 3, 1, 4], cmp)
[1, 2, 3, 4, 5]

where cmp() is the built-in function that compares two objects, x and y, and returns a negative number, 0 or a positive number depending on whether x<y, x==y, or x>y. During the course of the sort the relationships must stay the same for the final list to make sense.

If you want, you can define your own function for the comparison. For integers (and numbers in general) we can do:

>>> def numeric_compare(x, y):
>>>    return x-y
>>>

Or, more verbosely, but a little more understandable:

>>> def numeric_compare(x, y):
>>>    if x>y:
>>>       return 1
>>>    elif x==y:
>>>       return 0
>>>    else: # x<y
>>>       return -1
>>>
>>> a = [5, 2, 3, 1, 4]
>>> a.sort(numeric_compare)
>>> print a
[1, 2, 3, 4, 5]
