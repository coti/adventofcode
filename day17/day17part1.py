#!/usr/bin/env python

import sys


def parseLine( line, tab ):
    tab.append( int( line ) )
    return

def filled( containers, used ):
    liters = 0
    for i in range( len( used ) ):
        if used[i] > 0:
            liters += containers[i]
    return liters

def subsets( tab, fixed, obj ):
    comb = []    
    for i in (0, 1):
        new = fixed + [i]
        if len( new ) == len( tab ) or filled( tab, new ) >= obj:
            comb.append( new )
        else:
            comb+=  subsets( tab, new, obj ) 
    return comb

def eliminateWrongCombinations( containers, combinations, obj ):
    tab = []
    for c in combinations:
        if obj == filled( containers, c ):
            tab.append( c )
    return tab
    
def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1

    EGGNOG = 150
    containers = []

    fd = open( argv[1], 'r' ) 
    for line in fd:
        parseLine( line, containers )
    fd.close()

    combinations = subsets( containers, [], EGGNOG )
    combinations = eliminateWrongCombinations( containers, combinations, EGGNOG )
    print len( combinations ), "different combinations can fit all", EGGNOG, "liters of eggnog"

    return 
	
if __name__ == "__main__":
	count = main( sys.argv )
