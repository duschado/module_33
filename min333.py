#!/usr/bin/python3
import random
N = input('Enter the number N\n > ')
N = int(N)
lst_N = list()
for i in range(N):
	if i % 2 == 0 and i % 3 == 0:
		lst_N.append(i)
	if i % 2 != 0 and i % 5 == 0:
		lst_N.append(i)
print(lst_N)