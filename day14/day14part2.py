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

def getDistance( time, tab ):
    d = {}
    for reindeer in tab.keys():
        dist = distanceGone( time, reindeer, tab )
        d[reindeer] = dist
    return d

def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1

    FINALTIME = 2503
    
    tab = {}
    points = {}
    
    fd = open( argv[1], 'r' ) 
    for line in fd:
        parseLine( line, tab )
    fd.close()

    for reindeer in tab.keys(): 
        points[reindeer] = 0

    for t in range( 1, FINALTIME ):
        d = getDistance( t, tab )
        maxdistance = max( d.values() )
        for reindeer, distance in d.iteritems(): 
            if distance == maxdistance:
                points[reindeer] += 1

    winner = None
    mostpoints =  max( points.values() )
    for reindeer, points in points.iteritems(): 
        if points == mostpoints:
            winner = reindeer

    print winner, "is the farthest reindeer at time", FINALTIME, "after it has won", mostpoints, "points"
        
    return mostpoints
	
if __name__ == "__main__":
	count = main( sys.argv )
