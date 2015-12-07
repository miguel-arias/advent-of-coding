#!/usr/bin/env python

import sys, re

#day 5 advent of coding solution

def main(argv):
    puzzle_in = open(argv[0], 'r').read().split('\n')[:-1] #read in file input, split by newline into a list, get rid of last entry (its blank)
    #print puzzle_in

    nice = 0
    for item in puzzle_in:
	#if re.match("[a-zA-Z]*[aeiou][a-zA-Z]*[aeiou][a-zA-Z]*[aeiou][a-zA-Z]*", item) and re.search("([a-zA-Z])\\1+", item) and not re.search("(ab)+|(cd)+|(pq)+|(xy)+", item): #PART 1
	if re.search("(.).\\1", item) and re.search("(..).*\\1", item):
   	    nice += 1

    print nice

if __name__ == "__main__":
    main(sys.argv[1:]) 
