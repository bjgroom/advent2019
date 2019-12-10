#! /usr/bin/python3

from filein import filein

class Wire:
	def __init__(self, x, y):
		self.x = [x]
		self.y = [y]
		self.grid = set()
		
	def trace(self, d):
		if d[0] == 'U':
			upmove = self.y[-1] + int(d[1:])
			for n in range(self.y[-1], upmove):
				self.grid.add((self.x[-1], n))
			self.x.append(self.x[-1])
			self.y.append(upmove)
		elif d[0] == 'D':
			dnmove = self.y[-1] - int(d[1:])
			for n in range(self.y[-1], dnmove, -1):
				self.grid.add((self.x[-1], n))
			self.x.append(self.x[-1])
			self.y.append(dnmove)
		elif d[0] == 'L':
			lmove = self.x[-1] - int(d[1:])
			for n in range(self.x[-1], lmove, -1):
				self.grid.add((n, self.y[-1]))
			self.x.append(lmove)
			self.y.append(self.y[-1])
		elif d[0] == 'R':
			rmove = self.x[-1] + int(d[1:])
			for n in range(self.x[-1], rmove):
				self.grid.add((n, self.y[-1]))
			self.x.append(rmove)
			self.y.append(self.y[-1])
one = Wire(0, 0)
two = Wire(0, 0)

f = open("input3.txt").readlines()

first = f[0].strip().split(',')
second = f[1].strip().split(',')
vals = []

for d in first:
	one.trace(d)
for d in second:
	two.trace(d)
for v in one.grid.intersection(two.grid):
	if v != (0, 0):
		vals.append((abs(v[0])+abs(v[1])))
print(min(vals))
