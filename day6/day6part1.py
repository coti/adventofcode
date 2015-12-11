#!/usr/bin/env python

import sys

def initGrid( dims ):
	g = [ ]
	for i in range( dims[0] ):
		g.append( [0 for j in range( dims[1] ) ] )
	return g

def printGrid( grid ):
	for i in grid:
		print i
	return

def toggle( g, b, e ):
        bx,by = b
        ex,ey = e
        for i in range( int(bx), int(ex)+1 ):
                for j in range( int(by), int(ey)+1 ):
                        g[i][j] = (g[i][j]+1)%2
	return

def turnon( g, b, e ):
	bx,by = b
	ex,ey = e
	for i in range( int(bx), int(ex)+1 ):
		for j in range( int(by), int(ey)+1 ):
			g[i][j] = 1
        return

def turnoff( g, b, e ):
	bx,by = b
        ex,ey = e
        for i in range( int(bx), int(ex)+1 ):
                for j in range( int(by), int(ey)+1 ):
                        g[i][j] = 0
        return

def handleInstruction( s, grid ):
	ins = s.split( ' ' )
	begin = ins[-3].split( ',' )
	end = ins[-1].split( ',' )
	if ins[0] == "toggle":
		toggle( grid, begin, end )
	elif ins[0] == "turn":
		if ins[1] == "on":
			turnon( grid, begin, end )
		elif ins[1] == "off":
			turnoff( grid, begin, end )
		else:
			print "Error - wrong instruction", s
	else:
		print "Error - wrong instruction", s
	return

def countLightsOn( g ):
	nb = 0
	for i in g:
		for j in i:
			nb = nb + j
	return nb

def main( argv ):
	DIMENSIONS = (1000,1000)
	grid = initGrid( DIMENSIONS )
	
	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	fd = open( argv[1], 'r' ) 
	nb = 0
	for line in fd:
		handleInstruction( line, grid )
	fd.close()

	nb = countLightsOn( grid )
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
