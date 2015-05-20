'''A module for demonstrating exceptiosn.'''


def convert(s):
	'''Convert to an integer.'''
	try:
	 	return int(s)
	except (ValueError, TypeError):
		return -1
