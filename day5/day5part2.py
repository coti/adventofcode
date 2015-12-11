#!/usr/bin/env python

import sys

def findPairs( s ):
	res = []
        for i in range( 1, len(s ) ):
        	res.append( ( s[i-1:i+1], i ) )
        return res

def findTwiceInARow( s ):
	for p, i in findPairs( s ):
		if p in s[i+1:]:
			return True

def repeatsWithInterm( s ):
	for i in range( len(s)-2):
		if s[i] == s[i+2]:
			return True

def isNice( s ):
	if not findTwiceInARow( s ):
		return False
	if not repeatsWithInterm( s ):
		return False
	return True

def main( argv ):
	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	nb = 0
	fd = open( argv[1], 'r' ) 
	for line in fd:
		if isNice( line ):
			nb = nb + 1
	fd.close()
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
