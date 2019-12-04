#! /usr/bin/python3

def filein():

	# Returns a tuple full of the file contents

	path = input("What is the full path to your input file? ")
	f = open(path, 'r')
	return f.readlines()

