#!/usr/bin/python3
""" adding integers module """

def add_integer(a, b=98):
	""" function that check type of a and b and return the sum """ 
	if (type(a) not in [int, float]):
		raise TypeError("a must be an integer")
	if (type(b) not in [int, float]):
		raise TypeError("b must be an integer")
	a = int(a)
	b = int(b)
	return (a + b)
