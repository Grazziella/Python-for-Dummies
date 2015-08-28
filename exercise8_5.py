#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 8.5 Write a program to read through the mail box data and when you
# find line that starts with “From”, you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on
# the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.

def fromcount():

	f = raw_input('Enter a file: ')
	openfile = open(f)
	count = 0

	for line in openfile:

		filelist = line.split()

		if len(filelist) == 0: continue

		if filelist[0] == 'From':

			count = count + 1

			print(filelist[1])

	print(count)

if __name__ == '__main__':
	fromcount()
