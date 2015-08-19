#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 5.2 Write another program that prompts for a list of numbers as exercise 5.1
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

def max_min_number():

	total = 0
	count = 0
	num = 'notdone'
	max_number = None
	min_number = None

	while num != 'done':
		num = raw_input('Enter a number: ')

		try:
			num = int(num)

			total = total + int(num)
			count = count + 1

			if num > max_number:
				max_number = num
			if min_number is None or min_number > num:
				min_number = num

		except:
			print('Invalid input')

	print('total: ' + str(total),
		  'count: ' + str(count),
		  'maximum: ' + str(max_number),
		  'minimum: ' + str(min_number))

if __name__ == '__main__':
	max_min_number()
