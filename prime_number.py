#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a neanderthal way:
def prime_number(x):

	"""Return True if the number is prime, otherwise False!"""

	if x == 2 or x == 3 or x == 5 or x == 7 or x == 11:
		return 'True'

	elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
		return False

	else:
		return True

# another way:

def prime_number(num):

	if num < 2:
		return False

	for i in range(2, num):
		if num % i == 0:
			return False

	return True
