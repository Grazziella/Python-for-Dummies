#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 6.1 Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.

def backwards(string):

	index = 0
	while index < len(string):

		index = index + 1
		print(string[len(string) - index])

if __name__ == '__main__':
	backwards('Banana')
