#!/usr/bin/env python

import sys
import md5

def startsWithZeros( h ):
	if len( h ) < 6:
		print "The hash is too short"
		return None
	for c in h[:6]:
		if c != '0':
			return False
	return True

def getHash( secret, number ):
        m = md5.new()
        m.update( secret )
        m.update( str( number ))
        myhash = m.hexdigest()
	return myhash

def main( argv ):
        if 1 == len( argv ):
                print "Please enter puzzle input"
                return -1

	secret = argv[1]
	nb = 0
	while not startsWithZeros( getHash( secret, nb ) ):
		nb = nb + 1
	print nb

if __name__ == "__main__":
	main( sys.argv )
