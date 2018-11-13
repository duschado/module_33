#!/usr/bin/python3
import random

def replacement(i, j):
	"""Recursive listing of the list."""

	if i < j:
		lst[i], lst[j] = lst[j], lst[i]
		
		replacement(i + 1, j - 1)


n = input('Enter the number of items in the list\n > ')
n = int(n)

a, b = 0, n - 1

lst = random.sample(range(1, 100), n)
print("Input list: {}".format(lst))

replacement(a, b)
print("Output list: {}".format(lst))