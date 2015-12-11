#!/usr/bin/env python

import sys

def surfaceToCover( l, w, h ):
	s1 = l*w
	s2 = w*h
	s3 = h*l
	slack = min( [s1,s2,s3] )
	return 2*s1 + 2*s2 + 2*s3 + slack

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
			nb = nb + surfaceToCover( int(l), int(w), int(h) )
	fd.close()
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
