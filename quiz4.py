#1.
def fib(num):
	pred, curr = 0, 1
	k = 1
	while k < num:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr
print(fib(5))

#2.
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(5))

#3. The DRY principle means Dont Repeat Yourself so you can implement a process once but execture it many times
#4.
from math import pi 
def area_square(r):
	assert r > 0, 'A length must be positive'
	return r * r 

#5.
def area_circle(r):
	assert r > 0, 'A length must be positive'
	return r * r * pi 

#6.
def area_hexagon(r):
	assert r > 0, 'A length must be positive'
	return r * r * 3 * sqrt(3) / 2
#7.
def area(r, shape_constant):
	assert r > 0, 'A length must be positive'
	return r * r * shape_constant 

def area_square_2(r):
	return area(r, 1)

def area_circle_2(r):
	return area(r, pi)

def area_hexagon_2(r):
	return area(r, 3 * sqrt(3) / 2)
#8.
def identity(k):
	return k

def cube(k):
	return pow(k,3)

def summation(n, term):
	"""Sum the first N terms of a sequence.

	>>> summation(4, cube)
	200
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total
def sum_naturals(n):
	"""Sum the first N natural numbers

	>>> sum_natural_nums(4)
	10
	"""
	return summation(n, identity)
def sum_cubes(n):
	"""Sum the first N cubes of natural numbers.

	>>> sum_cubes (4)
	200
	"""
	return summation(n, cube)

#9.
def make_adder(k):
	"""Returns a function that takes one argument K and returns K + N"""

	def adder(k):
		return k + n
	return adder 
	


#10. 
square = lambda x: x * x
#11. A return statement ends the function call and determines the value of the call expression
#12. A control statement is a function that works as an if statement
