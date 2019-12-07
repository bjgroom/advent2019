#! /usr/bin/python3

import filein

class Wire:
	def __init__(self, x, y):
		self.x = [x]
		self.y = [y]
one = Wire(0, 0)

print(str(one.x)+str(one.y))	
