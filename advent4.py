#!/usr/bin/env python

import sys, re, md5

#advent of coding day 4 puzzle solution

def main(argv):
    #key = "iwrupvqb"
    key = argv[0]
    inc = 0
    pickaxe = key + str(inc)
    m = md5.new(pickaxe)
    print m.hexdigest()
    while not re.search("^000000", m.hexdigest()): #get rid of a zero for part 1 answer, im lazy
	inc += 1
	pickaxe = key + str(inc)
	print "Now: " + pickaxe
	m = md5.new(pickaxe)
	print m.hexdigest()
    print inc

if __name__ == "__main__":
    main(sys.argv[1:])
