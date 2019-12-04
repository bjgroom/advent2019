#! /usr/bin/python3

import filein, math

def fuelreq(mass):
	return (math.floor(int(mass)/3)-2)

masses = filein.filein()
total = 0
newmass = 0
for l in masses:
	newmass = fuelreq(l)		      # Initial condition
	total += newmass		      # Initial add of module fuel requirement
	while (newmass > 8):	      # Fuel cost of mass <= 8 is 0
		total += fuelreq(newmass)     # Add fuel cost of fuel itself
		newmass = fuelreq(newmass)    # Iterate

print('Fuel required: ' + str(total))
