# Exercise 4.6 

def computepay(hours, rate):
	if hours > 40:
		overtime = hours - 40
		overtime_rate = rate * 1.5
		salary = (40 * rate) + (overtime * overtime_rate)
	else:
		salary = hours * rate
	return salary
print(computepay(45, 10))
