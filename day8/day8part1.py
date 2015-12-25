#!/usr/bin/env python

import sys

def countCharacters( line, escape ):
    tot = len( line )
    escaped = 2
    double = False
    for i in range( 1, tot-1 ):
        if line[i] == escape:
            if not double:
                if line[i+1] == '\"':
                    escaped += 1
                elif line[i+1] == '\\':
                    double = True
                    escaped += 1
                elif line[i+1] == 'x':
                    escaped += 3
            else:
                double = False
    
    return escaped

def main( argv ):
    ESCAPE = "\\"
    
    if 1 == len( argv ):
        print "Please enter input file"
        return -1
    
    total, data = (0,0)
    nb = 0
    fd = open( argv[1], 'r' ) 
    for line in fd:
        l = line.split("\n")[0]
        nb +=  countCharacters( l, ESCAPE )
    fd.close()
    
    print nb
    return nb
	
if __name__ == "__main__":
	count = main( sys.argv )
