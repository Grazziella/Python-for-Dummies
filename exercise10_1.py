#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 10.1 Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

def max_mail():

	f = raw_input('Enter a file: ')
	opf = open(f)
	mail_list = []
	mail_dict = {}

	for line in opf:

		if line.startswith('From '):
			mail_list = line.split()
			mail_dict[mail_list[1]] = mail_dict.get(mail_list[1], 0) + 1

	m_list = []

	for mail, number in mail_dict.items():

		m_list.append((number, mail))

	m_list.sort(reverse = True)

	print(m_list[0])



if __name__ == '__main__':
		max_mail()
