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

def fib(num):
	pred, curr = 0, 1
	k = 1
	while k < num:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr
print(fib(5))

"""2.
3. The DRY principle means Dont Repeat Yourself so you can implement a process once but execture it many times
4.
5.
6.
7.
8.
9.
10. square = lambda x: x * x
11. A return statement ends the function call and determines the value of the call expression
12. A control statement is a function that works as an if statement
"""
