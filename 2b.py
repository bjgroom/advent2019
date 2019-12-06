#! /usr/bin/python3

from filein import filein
import csv

for noun in range(0, 100):
	for verb in range(0,100):

		cmds = next(csv.reader(open("input2.txt", 'r'))) # You now have a list of values as strings
		for c in range(0, len(cmds)):
			cmds[c] = int(cmds[c]) # Cast as integers
		cmds[1] = noun
		cmds[2] = verb
		for c in range(0, len(cmds), 4):
			if cmds[c] == 1: # Case 1: adding
				cmds[cmds[c+3]] = cmds[cmds[c+1]] + cmds[cmds[c+2]]
			elif cmds[c] == 2: # Case 2: multiplying
				cmds[cmds[c+3]] = cmds[cmds[c+1]] * cmds[cmds[c+2]]
			elif cmds[c] == 99: # Case 3: break
				if cmds[0] == 19690720:
					print("100 * noun + verb is: " + str(100*noun+verb))
					quit()
				else:
					break
