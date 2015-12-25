#!/usr/bin/env python

import sys
import string


def getIdx( c, s ):
    i = 0
    for p in s:
        if p == c:
            return i
        else:
            i = i+1
    print "Char ", c, "not found in string", s
    return -1

def incrementLetter( l ):
    lower = string.ascii_lowercase
    id = getIdx( l, lower )
    if id >= len( lower ):
        print "Letter already at max"
        return ""
    return lower[id+1]

def incrementPassword( p ):
    idx = len( p ) - 1
    done = False

    np = []
    
    while idx >= 0:
        if not done:
            while p[idx] == 'z':
                np.append( 'a' )
                idx -= 1                
            if idx > 0:
#                if idx < 4:
#                    print p[:idx], incrementLetter( p[idx] ), "".join( ["a" for i in range( idx+1, len(p ))] )
                np.append( incrementLetter( p[idx] ) )
                done = True
                idx -= 1
            else:
                print "Password already at max"
                return ""
        else:
            np.append( p[idx] )
            idx -= 1

    np = "".join( reversed( np ) )
    return np

def containsForbiddenLetters( s ):
    if "l" in s:
        return True
    elif "o" in s:
        return True
    elif "i" in s:
        return True
    else:
        return False

def containsTwoPairs( s ):
    lower = string.ascii_lowercase
    nb = 0
    for l in lower:
        ll = "".join( [l, l])
        if ll in s:
            nb += 1
            if nb == 2:
                return True
    return False

def hasIncreasing( s ):
    idx = 0
    while idx < len(s) - 2:
        if s[idx+1] != "z" and s[idx] != "y"  and s[idx] != "z":
            l1 = s[idx+2]
            l2 = incrementLetter( s[idx+1] )
            l3 = incrementLetter( incrementLetter( s[idx] ) )
            if l1 == l2 and l2 == l3:
                return True
        idx += 1
    return False
        
def isCorrect( password ):
    if not hasIncreasing( password ):
        return False
    if containsForbiddenLetters( password ):
        return False
    if not containsTwoPairs( password ):
        return False
    return True

def main( argv ):
    
    if 1 == len( argv ):
        print "Please enter puzzle input"
        return -1
    
    puzzle = argv[1]

    puzzle = incrementPassword( puzzle )
    while not isCorrect( puzzle ):
        puzzle = incrementPassword( puzzle )
        
    print puzzle
        
if __name__ == "__main__":
    main( sys.argv )
