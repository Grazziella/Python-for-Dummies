#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 8.1 Write a function called chop that takes a list and modifies it, removing
# the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(list_name):

	first = list_name.remove(list_name[0])
	last = list_name.remove(list_name[-1])

	return first, last, list_name


def middle(list_name):

	return list_name[0:len(list_name)]


fruits = ['apple', 'banana', 'strawberry', 'blueberry', 'mango', 'pear']

if __name__ == '__main__':
	print(chop(fruits))
	print(middle(fruits))
