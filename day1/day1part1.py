#!/usr/bin/env python

import sys

def countParenthesis( s ):
	cnt = 0
	for c in s:
		if c == '(':
			cnt = cnt + 1
		elif c == ')':
			cnt = cnt - 1
		else:
			if c != "\n" and c != " ":
				print "Wrong character:", c
	return cnt

def main( argv ):
	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	fd = open( argv[1], 'r' ) 
	nb = 0
	for line in fd:
		nb = nb + countParenthesis( line )
	fd.close()
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
