#!/usr/bin/env python

import sys, re

#day 8 solution

def main(argv):
    puzzle_in = open(argv[0], 'r').read().split('\n')[:-1]
    code_char = 0
    literal_char = 0

    for item in puzzle_in:
	code_char += len(item) #this is the easy part
	literal_char += len(eval(item)) #evaluate the string to make a string literal, count the length of that

    print "Characters of code: %s" % code_char
    print "Characters of literal chars: %s" % literal_char
    difference = code_char - literal_char
    print "Difference: %s" % difference

    
if __name__ == "__main__":
    main(sys.argv[1:])
