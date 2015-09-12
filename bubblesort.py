#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
def sort(l):

  	"""Return a sorted list. You can't use python sort method"""

	for num in range(len(l)-1, 0, -1):
		for i in range(num):
		
			if l[i] > l[i + 1]:
				n = l[i]
				l[i] = l[i + 1]
				l[i + 1] = n
	return l


if __name__ == '__main__':
    print(sort([500, -3, 50, 10, 0, 1, 20, 35, 800, 1000, 1001, 4]))
