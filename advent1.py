#!/usr/bin/env python

#advent of code day 1 puzzle 1

import sys

def main(argv):
    print argv[0]
    puzzle_in = open(argv[0], 'r')
    floor = 0
    position = 0 #part 2 stuff
    while True: 
	char = puzzle_in.read(1)
	position = position + 1
    	print char
	if char == "(":
	    floor = floor + 1
	elif char == ")":
	    floor = floor - 1
	else:
	    break
	if floor == -1: #uncomment this if statement section if you want part 1 answer
	    print position
	    break
    print floor

if __name__ == "__main__":
    main(sys.argv[1:])
