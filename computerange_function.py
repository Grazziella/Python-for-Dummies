# Exrecise 4.7

def computegrade():
	score = raw_input('Enter score: ')
	try:
		score = float(score)
	except:
		score = 2
	if score > 1.0 or score < 0:
		print('Error: score out of range! ')
	elif score >= 0.9:
		print('A')
	elif score >= 0.8:
		print('B')
	elif score >= 0.7:
		print('C')
	elif score >= 0.6:
		print('D')
	elif score < 0.6:
		print('F')
computegrade()
