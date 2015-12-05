#!/usr/bin/env python

#Day 3 challenge solution

import sys

def main(argv):
    puzzle_in = open(argv[0], 'r')
    
    unique_houses = 0
    x = y = 0
    robo_x = robo_y = 0
    turn = 0
    visited_houses = {} #makes the houses visited a dictionary
    visited_houses[x,y] = 1 #this way if a house is visited twice there is still only one entry in the dictionary for it
 
    while True:
	char = puzzle_in.read(1)
	if char == "^":
	    if turn % 2:
	        y += 1
	    else:
		robo_y += 1
	elif char == "v":
	    if turn % 2:
	    	y -= 1
	    else:
		robo_y -= 1
	elif char == ">":
	    if turn % 2:
	    	x += 1
	    else:
		robo_x += 1
	elif char == "<":
	    if turn % 2:
	    	x -= 1
	    else:
		robo_x -= 1
	else:
	    break
	if turn % 2:
	    visited_houses[x,y] = 1
	else:
	    visited_houses[robo_x,robo_y] = 1
	turn += 1

    for i in visited_houses:
	unique_houses += 1

    print unique_houses

if __name__ == "__main__":
    main(sys.argv[1:])

    
    
