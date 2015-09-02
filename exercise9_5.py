#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 9.5 This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the
# whole email address). At the end of the program, print out the contents of your
# dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

def domain():

	f = raw_input('Enter a file: ')
	opf = open(f)
	mailist = []
	maildict = {}

	for line in opf:

		if line.startswith('From '):

			line.split()

			att = line.find('@')

			end = line.find(' ', att)
			
			mailist = line[(att + 1):end]

			maildict[mailist] = maildict.get(mailist, 0) + 1

	return maildict


if __name__ == '__main__':
	print(domain())
