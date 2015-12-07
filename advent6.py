#!/usr/bin/env python

import sys, re

#advent of coding day 6 puzzle solution

def main(argv):
    puzzle_in = open(argv[0], 'r').read().split('\n')[:-1]
    lights = 0
    grid = {}
    for item in puzzle_in:
	m = item.split(' through ')
	end = m[-1]
	start = m[0].split(' ')[-1]
	action = m[0].split(' ')[:-1]
	tempx = startx = int(start.split(',')[0])
	tempy = starty = int(start.split(',')[-1])
	endx = int(end.split(',')[0]) + 1
	endy = int(end.split(',')[-1]) + 1

	print "%s %s %s" % (' '.join(action), start, end)
	while starty != endy:
	    while tempx != endx:
		try:
		    if action[-1] == 'on':
		    	grid[tempx,starty] += 1
		    elif action[-1] == 'off':
		    	grid[tempx,starty] -= 1
		    	if grid[tempx, starty] < 0:
			    grid[tempx, starty] = 0
		    elif action[-1] == 'toggle':
		    	grid[tempx,starty] += 2
		except KeyError:
		    if action[-1] == 'on':
			grid[tempx, starty] = 1
		    elif action[-1] == 'off':
			grid[tempx, starty] = 0
		    elif action[-1] == 'toggle':
			grid[tempx, starty] = 2
		tempx += 1
		print "%s,%s" % (tempx, starty)
	    tempx = startx
	    starty += 1
	    print "%s,%s" % (tempx, starty)
    for item in grid.values():
	lights += item

    print lights

if __name__ == "__main__":
    main(sys.argv[1:])
