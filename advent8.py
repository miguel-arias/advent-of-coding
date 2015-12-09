#!/usr/bin/env python

import sys, re

#day 8 solution

def main(argv):
    puzzle_in = open(argv[0], 'r').read().split('\n')[:-1]
    code_char = 0
    literal_char = 0
    encode_char = 0 #part 2

    for item in puzzle_in:
	code_char += len(item) #this is the easy part
	literal_char += len(eval(item)) #evaluate the string to make a string literal, count the length of that

    print "Characters of code: %s" % code_char
    print "Characters of literal chars: %s" % literal_char
    difference = code_char - literal_char
    print "Part 1 Difference: %s" % difference

    
    #part 2

    for item in puzzle_in:
	encode_string = '"' #start off with a double quote
	for char in item:
	    if char == '"':
		encode_string += '\\"'
	    elif char == '\\':
		encode_string += '\\\\' #add an extra escape char
	    else:
		encode_string += char
	encode_string += '"' #close the double quote
#	print item
#	print encode_string
	encode_char += len(encode_string)

    print "Characters of encode chars: %s" % encode_char
    difference2 = encode_char - code_char
    print "Part 2 Difference: %s" % difference2	

if __name__ == "__main__":
    main(sys.argv[1:])
