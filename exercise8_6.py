#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 8.6 Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0


def max_min_num():

	num_list = []

	while True:

		num = raw_input('Enter a number: ')

		if num == 'done': break

		num_list.append(num)

	maxi = float(max(num_list))
	mini = float(min(num_list))

	print('Maximum: ' + str(maxi))
	print('Minimum: ' + str(mini))

if __name__ == '__main__':
	max_min_num()
