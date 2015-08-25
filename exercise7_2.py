#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 7.2 Write a program to prompt for a file name, and then read through
# the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

def spam_confidence():

	file_name = raw_input('Enter a file name: ')

	xfile = open(file_name)

	total_confidence = 0

	for line in xfile:
		
		if line.startswith('X-DSPAM-Confidence'):

			point = line.find(':')
		
			total_confidence = total_confidence + float(line[point + 1:])

	print('Average spam confidence: ' + str(total_confidence))


if __name__ == '__main__':
	spam_confidence()
