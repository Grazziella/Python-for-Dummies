#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 9.2 Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

def dow():

	f = raw_input('Enter a file: ')
	opf = open(f)
	dow = {}
	mail_list = []

	for line in opf:

		if line.startswith('From'):

			mail_list = line.split()

			if len(mail_list) < 3: continue

			dow[mail_list[2]] = dow.get(mail_list[2],0) + 1

	return dow

if __name__ == '__main__':
	print(dow())
