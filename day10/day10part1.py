#!/usr/bin/env python

import sys


def lookandsay( sequence ):
    res = ""
    i = 0
    while i < len( sequence ):
        ahead = 1
        while (i + ahead < len( sequence )) and ( sequence[i] == sequence[i+ahead]):
            ahead += 1
        res += str( ahead ) + str( sequence[i] )
        i += ahead
    return res

    
def main( argv ):
    NBITER = 40
    
    if 1 == len( argv ):
        print "Please enter puzzle input"
        return -1
    
    puzzle = argv[1]
    for i in range( NBITER ):
        puzzle = lookandsay( puzzle )

    print len( puzzle )
        
if __name__ == "__main__":
    main( sys.argv )
