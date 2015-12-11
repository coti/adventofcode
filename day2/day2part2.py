#!/usr/bin/env python

import sys

def ribbon( l, w, h ):
	bow = l*w*h
	p1 = 2*l + 2*w
	p2 = 2*l + 2*h
	p3 = 2*w + 2*h
	wrap = min( [p1,p2,p3] )
	return wrap + bow

def dimensions( s ):
	if s == "\n":
		return ( -1, -1, -1 )
	s = s.split( "\n")[0]
	return s.split( "x" )

def main( argv ):
	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	fd = open( argv[1], 'r' ) 
	nb = 0
	for line in fd:
		(l,w,h) = dimensions( line )
		if (l,w,h) != (-1,-1,-1):
			nb = nb + ribbon( int(l), int(w), int(h) )
	fd.close()
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
