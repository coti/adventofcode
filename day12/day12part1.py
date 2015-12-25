#!/usr/bin/env python

import sys
import re

def getAllNumbers( s ):
    p = re.compile('[+-]?[0-9]+')
    n = p.findall( s )
    return n

def addAll( tab ):
    n = 0
    for t in tab:
        n += int( t )
    return n

def addNumbers( s ):
    t = getAllNumbers( s )
    nb = addAll( t )
    return nb

def main( argv ):
    
    distances = {}

    if 1 == len( argv ):
        print "Please enter input file"
        return -1
    
    d = []
    
    total, data = (0,0)
    nb = 0
    fd = open( argv[1], 'r' ) 
    for line in fd:
        nb += addNumbers( line )
    fd.close()
    
    print nb
    return nb
	
if __name__ == "__main__":
	count = main( sys.argv )
