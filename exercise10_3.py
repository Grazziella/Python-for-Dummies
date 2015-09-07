#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 10.3 Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctuation,
# or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.

def count_letters():

	f = raw_input('Enter a file: ')
	opf = open(f)
	l_letters = []
	letters = {}
	import string

	for line in opf:

		line.split()
		line = line.translate(None, string.punctuation)
		line = line.translate(None, string.digits)
		line = line.lower()
		line = line.strip()
		line = line.replace(' ', '')

		for letter in line:
			
			if letter not in letters:
				letters[letter] = 1

			else:
				letters[letter] = letters[letter] + 1

	for l, num in letters.items():

		l_letters.append((num, l))
		l_letters.sort(reverse = True)

	for num, l in l_letters:
		print l

if __name__ == '__main__':
	count_letters()
