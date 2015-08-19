#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse_str(name):

	""" Return the reverse string. """

	rev_name = ''

	for n in range(len(name)):
		rev_name += name[-1 - n] 

	return rev_name

if __name__ == '__main__':
	print(reverse_str('Arara'))
