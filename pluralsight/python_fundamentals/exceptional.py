'''A module for demonstrating exceptiosn.'''


def convert(s):
	'''Convert to an integer.'''
	x = -1
	try:
		x = int(s)
	except (ValueError, TypeError):
	return x
