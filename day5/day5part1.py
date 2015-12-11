#!/usr/bin/env python

import sys

def countVowels( s ):
	vowels = "aeiou"
	nb = 0
	for c in s:
		if c in vowels:
			nb = nb + 1
	return nb

def twiceInARow( s ):
	for i in range( 1, len(s ) ):
		if s[i] == s[i-1]:
			return True
	return False

def forbiddenSubstring( s ):
	forbid = [ "ab", "cd", "pq", "xy" ]
	for f in forbid:
		if f in s:
			return True

def isNice( s ):
	if countVowels( s ) < 3:
		return False
	if not twiceInARow( s ):
		return False
	if forbiddenSubstring( s ):
		return False
	return True

def main( argv ):
	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	fd = open( argv[1], 'r' ) 
	nb = 0
	for line in fd:
		if isNice( line ):
			nb = nb + 1
	fd.close()
	print "Total:", nb
	return nb

if __name__ == "__main__":
	count = main( sys.argv )
