#!/usr/bin/python3

def fibonacci(f2, f1):
	"""Recursive generating Fibonacci sequence to N."""

	f = f2 + f1
	if f < N:
		fib_sequence.append(f)		
		fibonacci(f1, f)

N = input('Enter the number N\n > ')
N = int(N)

F2, F1 = 0, 1
fib_sequence = [0, 1]

fibonacci(F2, F1)
print("Fibonacci sequence: {}".format(fib_sequence))