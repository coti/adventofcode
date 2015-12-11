#!/usr/bin/env python

import sys


def addPresent( grid, coords ):
	if coords in grid.keys():
		grid[coords] = grid[coords] + 1
	else:
		grid[coords] = 1
	return

def move( c, coord ):
        x, y = coord
        if c == '>':
        	x = x + 1
        elif c == "<":
                x = x - 1
        elif c == '^':
                y = y - 1
        elif c == 'v':
                y = y + 1
        else:
                if c != "\n" and c != " ":
                	print "Unexpected character: ", c
	return x, y

def countHouses( grid ):
	return len( grid.keys() ) 

def main( argv ):

	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	grid = {}
	coords = (0,0)
	addPresent( grid, coords )
	print grid

	fd = open( argv[1], 'r' ) 
	for line in fd:
		for c in line:
			coords = move( c, coords )
			addPresent( grid, coords )

	fd.close()
	nb = countHouses( grid )
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
