#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 10.2 This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the “From” line by finding the
# time string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.
# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6

def hours():

	opf = open('mbox-short.txt')
	list_hours = []
	d_mail = {}

	for line in opf:

		if line.startswith('From '):
			list_hours = line.split()
			h = list_hours[5]
			time = h[:h.find(':')]
			d_mail[time] = d_mail.get(time, 0) + 1


	t_mail = d_mail.items()
	t_mail.sort()

	for ht in t_mail:

		print(ht)

if __name__ == '__main__':
	hours()		
