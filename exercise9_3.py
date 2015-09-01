#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 9.3 Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

def sender():

	f = raw_input('Enter a file: ')
	opf = open(f)
	mail_l = list()
	mail_d = dict()

	for line in opf:

		if line.startswith('From'):

			mail_l = line.split()

			if len(mail_l) < 2: continue

			mail_d[mail_l[1]] = mail_d.get(mail_l[1], 0) + 1

	print(mail_d)

if __name__ == '__main__':
	sender()
