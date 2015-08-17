#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prime_number(x):

	"""Return True if the number is prime, otherwise False!"""

	if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
		return 'True'

	elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
		return 'False'

	else:
		return 'True'

if __name__ == '__main__':
	print(prime_number(2))
