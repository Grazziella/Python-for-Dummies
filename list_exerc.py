#!/usr/bin/env python
# -*- coding: utf-8 -*-

def first_element(list_name):

	"""Returns the first element of a list."""

	return list_name[0]


def last_element(list_name):

	"""Returns the last element of a list."""

	return list_name[-1]

def sum_list(list_name):

	"""Returns the sum of elements in a list of numbers."""

	total_sum = 0

	for element in list_name:

		total_sum = total_sum + element

	return total_sum


numbers = [50, 3.1, 45, 90, 100.1]
if __name__ == '__main__':
	print(first_element(numbers))
	print(last_element(numbers))
	print(sum_list(numbers))
