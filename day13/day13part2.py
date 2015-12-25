#!/usr/bin/env python

import sys
import itertools

def parseFile( line ):
    line = line.split( '.\n' )[0]
    tab = line.split( ' ' )
    a = tab[0]
    b = tab[-1]
    h = -1
    try:
        h = int(tab[3])
    except ValueError:
        print "happyness", tab[3], "error"
        return None
    if tab[2] == "lose" :
        h = -h
    return a, b, h

def insertSelf( tab ):
    insertPersonInTheTable( "Myself", tab )
    return

def insertPersonInTheTable( p, tab ):
    if p not in tab[0]:
        tab[0].append( p )
        for l in tab[1:]:
            l.append( 0 )
        tab.append( [0 for x in range( len( tab[0] )+1 ) ] )
        tab[-1][0]  = p
    return

def printTable( tab ):
    for l in tab:
        print l
    return
        
def findCoupleInTheTable( couple, tab ):
    a, b, h = couple
    
    insertPersonInTheTable( a, tab )
    insertPersonInTheTable( b, tab )
    
    i = tab[0].index( a )
    j = tab[0].index( b )

    return i+1, j+1
    
def insertCouple( couple, tab ):
    i, j = findCoupleInTheTable( couple, tab )
    h = couple[2]
    tab[i][j] = h
    return

def computeArrangements( tab ):
    arrangements = list( itertools.permutations( tab[0] ))
    return arrangements

def getHappinessOfCouple( couple, tab ):
    a, b = couple
    i = tab[0].index( a )
    j = tab[0].index( b )
    return tab[i+1][j+1]

def getHappinessOfArrangement( arr, tab ):
    h = 0
    for i in range( len( arr ) ):
        h += getHappinessOfCouple( ( arr[i-1], arr[i]), tab )
        h += getHappinessOfCouple( (arr[i], arr[i-1]), tab)
    return h
        
def getBestArrangement( arr, tab ):
    c = -1
    best = arr[0]
    for a in arr:
        n = getHappinessOfArrangement( a, tab )
        if n > c:
            c = n
            best = a
    return best, c
    
def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1
    
    nb = 0
    d = [[]]
    insertSelf( d )
    fd = open( argv[1], 'r' ) 
    for line in fd:
        couple = parseFile( line )
        insertCouple( couple, d )
    fd.close()

    arr = computeArrangements( d )
    a, c = getBestArrangement( arr, d )
    
    print c, "cost of", a
    return nb
	
if __name__ == "__main__":
	count = main( sys.argv )
