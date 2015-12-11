#!/usr/bin/env python

import sys

def getPosition( s, n, p ):
	for c in s:
		if c == '(':
			n = n + 1
			p = p + 1
		elif c == ')':
			n = n - 1
			p = p + 1
		else:
			if c != "\n" and c != " ":
				print "Wrong character:", c
		if n == -1 :
			print "Floor -1, position", p
			return n, p
	return n, p

def main( argv ):
	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	fd = open( argv[1], 'r' ) 
	nb = 0
	p = 0
	for line in fd:
		(nb,p) = getPosition( line, nb, p )
		if -1 == nb:
			break
	fd.close()
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
