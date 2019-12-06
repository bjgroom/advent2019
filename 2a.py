#! /usr/bin/python3

from filein import filein
import csv

cmds = next(csv.reader(open("input2.txt", 'r'))) # You now have a list of values as strings

# Initial Conditions

cmds[1] = '12'
cmds[2] = '2'

for c in range(0, len(cmds)):
	cmds[c] = int(cmds[c]) # Cast as integers

for c in range(0, len(cmds), 4):
	print("counter is " + str(c) + " and value is " + str(cmds[c]))
	
	if cmds[c] == 1: # Case 1: adding
		cmds[cmds[c+3]] = cmds[cmds[c+1]] + cmds[cmds[c+2]]
	elif cmds[c] == 2: # Case 2: multiplying
		cmds[cmds[c+3]] = cmds[cmds[c+1]] * cmds[cmds[c+2]]
	elif cmds[c] == 99: # Case 3: break
		break

print("The value at position 0 is: " + str(cmds[0]))
