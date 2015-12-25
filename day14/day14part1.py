#!/usr/bin/env python

import sys
import math

def parseLine( line, tab ):
    t = line.split( " " )
    name = t[0]
    speed = int( t[3] )
    duration = int( t[6] )
    rest = int( t[-2] )
    tab[name] = [ ( speed, duration ), ( 0, rest ) ]
    return

def getNbOfCyclesCompleted( time, duration, rest ):
    cycle = duration + rest
    return int( math.floor( time / cycle ) )

def distanceGone( time, name, tab ):
    [ ( speed, duration ), ( _, rest ) ] = tab[name]
    cycles = getNbOfCyclesCompleted( time, duration, rest )
    distance = cycles * duration * speed
    timeleft = time - ( cycles * ( duration + rest ) )
    distance += min( timeleft, duration ) * speed
    return distance

def getFarthestReindeer( time, tab ):
    name = None
    dist = -1

    for reindeer in tab.keys():
        d = distanceGone( time, reindeer, tab )
        if d > dist:
            dist = d
            name = reindeer
        
    return name, dist

def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1

    FINALTIME = 2503
    
    tab = {}
    
    fd = open( argv[1], 'r' ) 
    for line in fd:
        parseLine( line, tab )
    fd.close()

    farthest, distance = getFarthestReindeer( FINALTIME, tab )

    print farthest, "is the farthest reindeer at time", FINALTIME, "after it traveled", distance, "km."
    
    return distance
	
if __name__ == "__main__":
	count = main( sys.argv )
