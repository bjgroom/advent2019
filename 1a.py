#! /usr/bin/python3

import filein, math

masses = filein.filein()
total = 0
for l in masses:
	total += (math.floor(int(l)/3)-2)

print('Fuel required: ' + str(total))
