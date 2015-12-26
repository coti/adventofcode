#!/usr/bin/env python

import sys

def initAuntSue( name ):
    sue = {}
    sue['name'] = name
    return sue

def setCharac( name, key, value, tab ):
    tab[name-1][key] = int(value)
    return

def parseLine( line, tab ):
    line = line.split( "\n" )[0]
    name = int( line.split( ": " )[0].split( " ")[1] )
    charac =  (":".join( line.split( ": " )[1:] )).split( ", ")
    tab.append( initAuntSue( name ) )
    for c in charac:
        k, v = c.split( ":" )
        setCharac( name, k, v, tab )
    return

def compareAunt( aunt1, aunt2 ):
    match = True
    characteristics = sorted( set( aunt1.keys() + aunt2.keys() ) )
    for c in characteristics:
        if c in aunt1 and c in aunt2:
            if not c == "name":
                if aunt1[c] != aunt2[c]:
                    return False
    return match

def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1

    tab = []

    wrapping = { "children": 1, "cats": 7, "samoyeds": 2, "pomeranians": 3,"akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

    fd = open( argv[1], 'r' ) 
    for line in fd:
        parseLine( line, tab )
    fd.close()

    gift = tab[0]
    for aunt in tab:
        found = compareAunt( aunt, wrapping )
        if found:
            gift = aunt
            break

    print "The gift was from Aunt Sue", gift["name"]
    return 
	
if __name__ == "__main__":
	count = main( sys.argv )
