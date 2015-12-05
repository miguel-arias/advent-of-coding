#!/usr/bin/env python

#day 2 advent of coding challenge

import sys

def min(a, b):
    if a < b:
	return a
    else:
	return b

def max(a,b):
    if a > b:
	return a
    else:
	return b

def calcRibbon(dimensions): #part 2
    (length,width,height) = dimensions
    
    length = int(length)
    width = int(width)
    height = int(height)

    side1 = length*width
    side2 = width*height
    side3 = height*length

    sides = [length,width,height] 

    volume = length*width*height

    biggest = max(max(length, width), height)
    smallest = sec_smallest = biggest 
    for item in sides:
	if item < biggest:
	    sec_smallest = smallest
	    smallest = item
	elif item < sec_smallest and item >= smallest:
	    sec_smallest = item
    print "Smallest dimension: %s" % smallest
    print "Second smallest: %s" % sec_smallest
    perimeter = smallest + smallest + sec_smallest + sec_smallest
 
    print "Volume: %s" % volume
    print "Perimeter: %s" % perimeter

    ribbon = volume + perimeter
    print ribbon
    return ribbon

def calcWrappingPaper(dimensions): #part 1
    (length,width,height) = dimensions

    length = int(length) #convert strings to ints
    width = int(width)
    height = int(height)

    side1 = length*width
    side2 = width*height
    side3 = height*length

    smallest = min(min(side1,side2), side3)

    sa = 2*side1 + 2*side2 + 2*side3
    wrapping_paper = sa + smallest
    return wrapping_paper

def main(argv):
    puzzle_in = open(argv[0], 'r')
    square_feet = 0
    ribbon = 0
    presents = puzzle_in.read().split('\n')[0:-1] #read in all the lines of dimensions, split up by newlines, ommit last line cuz its blank
    for item in presents:
	print square_feet
	present = tuple(item.split('x'))
	print present
	wrapping_paper = calcWrappingPaper(present)
	rib_feet = calcRibbon(present)
	square_feet = square_feet + wrapping_paper
 	ribbon = ribbon + rib_feet
	print "Wrapping Paper: %s" % square_feet
    	print "Ribbon: %s" % ribbon
    print square_feet

if __name__ == "__main__":
    main(sys.argv[1:])
