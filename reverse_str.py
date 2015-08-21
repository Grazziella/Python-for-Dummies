#!/usr/bin/env python
# -*- coding: utf-8 -*-

# using for loop:

def reverse_str(name):

	""" Return the reverse string. """

	rev_name = ''

	for n in range(len(name)):
		rev_name += name[-1 - n] 

	return rev_name

if __name__ == '__main__':
	print(reverse_str('Arara'))

# using while loop:

def reverse_str(string):

	""" Return the reverse string. """	
	
	reverse = ''
	index = 0
	
	while index < len(string):

		index = index + 1
		reverse += string[len(string) - index]
		
	print(reverse)

if __name__ == '__main__':
	reverse_str('Banana')
