'''A module for demonstrating exceptiosn.'''


def convert(s):
	'''Convert to an integer.'''
	try:
	 	return int(s)
	except (ValueError, TypeError) as e:
		return -1
