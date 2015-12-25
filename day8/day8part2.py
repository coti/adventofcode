#!/usr/bin/env python

import sys

def encode( line ):
    tot = len( line )
    nb = 0
    newline = ["\""]
    for c in line:
        if c == "\"":
            newline.append( "\\" )
        elif c == "\\":
            newline.append( "\\" )
        newline.append( c )

    newline.append( "\"" )
        
    n = "".join( newline )
    return len( n ) - len( line )

def main( argv ):
    
    if 1 == len( argv ):
        print "Please enter input file"
        return -1
    
    total, data = (0,0)
    nb = 0
    fd = open( argv[1], 'r' ) 
    for line in fd:
        l = line.split("\n")[0]
        nb +=  encode( l )
    fd.close()
    
    print nb
    return nb
	
if __name__ == "__main__":
	count = main( sys.argv )
