def length(str):

	"""Return the number of characters in the string."""

	sum = 0
	for i in str:
		sum = sum + 1
	return sum

if __name__ == '__main__':
    print(length("LOVE YOU!"))
