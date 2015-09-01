#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 9.4 Add code to the above program to figure out who has the most messages
# in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section 5.7.2) to find who has the most
# messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

def max_sender():

	f = raw_input('Enter a file: ')
	opf = open(f)
	mail_l = []
	mail_d = {}

	for line in opf:

		if line.startswith('From'):

			mail_l = line.split()

			if len(mail_l) < 2: continue

			mail_d[mail_l[1]] = mail_d.get(mail_l[1], 0) + 1

	times = None
	
	for key in mail_d:

		if mail_d[key] > times:

			times = mail_d[key]

			mail_key = key

	print(mail_key + ' ' + str(times))

if __name__ == '__main__':
	max_sender()
