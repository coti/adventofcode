#!/usr/bin/env python

import sys

def parseLine( line, tab ):
    line = line.split( "\n" )[0]
    name, charac = line.split( ": " )
    it = charac.split( ", ")
    tab[name] = {}
    for i in it:
        elem = i.split( " " )
        tab[name][elem[0]] = int( elem[1] )
    return

def combinations( nb, fixed, obj ):
    ihave = sum( fixed )
    toset = nb - len( fixed )
    comb = []
    
    for i in range( obj - ihave + 1 ):
        new = list( fixed + [i] )
        if len( fixed ) == nb:
            if sum( fixed ) == obj:
                comb = comb + [fixed]
        else:
            comb = comb + combinations( nb, new, obj )    
            
    return comb

def computeCalories( recipe, tab ):
    calories = 0
    nbElems = len( recipe )
    for elem in range( nbElems ):
        name = tab.keys()[elem]
        calories += ( tab[name]["calories"] * recipe[elem] )
    return calories
        
def computeScore( recipe, tab ):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    nbElems = len( recipe )
    for elem in range( nbElems ):
        name = tab.keys()[elem]
        capacity += ( tab[name]["capacity"] * recipe[elem] )
        durability += ( tab[name]["durability"] * recipe[elem] )
        flavor += ( tab[name]["flavor"] * recipe[elem] )
        texture += ( tab[name]["texture"] * recipe[elem] )
        calories += ( tab[name]["calories"] * recipe[elem] )

    if calories != 500:
        return -1
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0
    return capacity * durability * flavor * texture

def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1

    tab = {}

    NBTSP = 100
    
    fd = open( argv[1], 'r' ) 
    for line in fd:
        parseLine( line, tab )
    fd.close()

    best = 0
    recipes = combinations( len( tab.keys()), [], NBTSP )
    for r in recipes:
        score = computeScore( r, tab )
        if score > best:
            best = score

    print best
    return best
	
if __name__ == "__main__":
	count = main( sys.argv )
