#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercise 8.4 Download a copy of the file from www.py4inf.com/code/romeo.txt
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in the
# list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']


def create():

	file_name = raw_input('Enter file: ')
	opened_file = open(file_name)
	words = []

	for line in opened_file:

		elements = line.split()

		for element in elements:

			if element not in words:

				list_words = words.append(element)

	words.sort()

	print(words)


if __name__ == '__main__':
	create()
