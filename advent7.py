#!/usr/bin/env python

import sys, re
from time import sleep

#advent of coding day 7 solution


def wireTing(puzzle_in):
    global wires
    for item in puzzle_in:
        #print item
        op = None
        a = None
        item = item.split(' ')
        out = item[-1] #output will always be the last item
        b = item[-3] #b will be 3rd to last (2nd to last is just ->)
        if wires.get(out) or wires.get(out) == 0:
            continue
        try:
            op = item[-4] #try to set op to the 4th to last in list. if it fails, we have a x -> number situation
            a = item[-5] #if this fails, we have a NOT statement
#           print "%s, %s, %s, %s" % (a, op, b, out)
            if (not wires.get(a) and not re.match("[0-9]+", a) and not wires.get(a) == 0) or (not wires.get(b) and not re.match("[0-9]+", b) and not wires.get(b) == 0): #need to check they're plain numbers too
                #print "not enough info"
                continue
            if re.match("[0-9]+", a):
                wires[a] = int(a)
            if re.match("[0-9]+", b):
                wires[b] = int(b)
            if op == "AND":
                wires[out] = wires[a] & wires[b]
            elif op == "OR":
                wires[out] = wires[a] | wires[b]
            elif op == "RSHIFT":
                wires[out] = wires[a] >> wires[b]
            elif op == "LSHIFT":
                wires[out] = wires[a] << wires[b]
            print "%s:%s, %s, %s:%s, %s" % (a, wires[a], op, b, wires[b], out)
            print "%s allocated: %s" % (out, wires[out])
#           sleep(1)
        except IndexError:
            if op:
                if not wires.get(b) and not re.match("[0-9]+", b) and not wires.get(b) == 0:
                    continue
		elif re.match("[0-9]+", b):
                    wires[out] = ~int(b, 16)
                else:
                    wires[out] = ~wires[b]
                print "%s, %s, %s" % (op, b, out)
                print "%s allocated: %s" % (out, wires[out])
            else:
		if out == 'b' and wires.get('b'):  #uncomment this for part 1 answer
		    continue
                if not wires.get(b) and re.match("[0-9]+", b): #if b is a number, just allocate it to out
                    wires[out] = int(b)
                elif wires.get(b): #if b is a wire, check if it has been allocated. if so, allocate it to out
                    wires[out] = wires[b]
                else: #otherwise, skip
                    continue
                print "%s, %s" % (b, out)
                print "%s allocated: %s" % (out, wires[out])
                sleep(1)


def main(argv):
    global wires
    wires = {}
    #wires["a"] = "DEFAULT"
    puzzle_in = open(argv[0], 'r').read().split('\n')[:-1]
    while not wires.get("a"): #use the .get() method of dictionary instead of trying to reference by index, otherwise will get a KeyError instead of None
	wireTing(puzzle_in)

    print "Part 1 answer: %s" % wires["a"]
    part1answer = wires["a"]
    

    #part 2
    print "\n\n\n\n\n\n\n\n\nPART 2\n\n\n\n\n\n\n\n"
    wires = {}
    wires["b"] = part1answer
    while not wires.get("a"):
	wireTing(puzzle_in)

    print "Part 2 answer: %s" % wires["a"]

if __name__ == "__main__":
    main(sys.argv[1:])	
