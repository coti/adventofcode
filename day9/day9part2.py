#!/usr/bin/env python

import sys

def insertDistance( d, a, c, tab ):
    if d not in tab.keys():
            tab[d] = [ {a: c } ]
    else:
        tab[d].append( {a: c })
    return

def fillTable( d, tab ):
    for line in d:
        cities, distance = line.split ( " = " )
        distance = int( distance )
        dep,arr = cities.split( " to " )

        insertDistance( dep, arr, distance, tab )
        insertDistance( arr, dep, distance, tab )
  
    return

def departureCities( tab ):
    return tab.keys()

def allCities( tab ):
    c = []
    for t in tab:
        c.append( t )
        for a in tab[t]:
            c.append( a.keys()[0] )
    c = sorted( set( c ))
    return c

def wentThroughAllTheCities( path, cities ):
    for c in cities:
        if c not in path:
            return False
    return True

def alreadyInThePath( city, path ):
    if city in path:
        return True
    else:
        return False

def destinations( city, tab ):
    d = []
    if not city in tab.keys():
        return []
    for a in tab[city]:
        d.append( a.keys()[0] )
    return d

def getPath( path, tab ):
    cc = path[-1]
    d = destinations( cc, tab )
    cities = allCities( tab )
    allpaths = []
    
    if wentThroughAllTheCities( path, cities ):
        return [path]
    if d == []:
        return [path]
    
    for nextcity in d:
        if not alreadyInThePath( nextcity, path ):
            t = path + [nextcity]
            p = getPath( t, tab )
            for p0 in p:
                allpaths.append( p0 )
    return allpaths

def getCost( d, a, tab ) :
    for n in tab[d]:
        if a in n.keys():
            return n[a]
        
    print "Destination", a, "not found from", d
    return None
    
def computeCost( path, tab ):
    cost = 0
    for i in range( len( path ) - 1) :
        cost += getCost( path[i], path[i+1], tab )

    return cost

def computePaths(  tab ):
    dep = departureCities( tab )
    cities = allCities( tab )
    listOfPaths = []
    
    for d in dep:
        p = getPath( [ d ], tab )
        for path in p:
            if wentThroughAllTheCities( path, cities ):
                listOfPaths.append( path )
        
    return listOfPaths

def main( argv ):
    
    distances = {}

    if 1 == len( argv ):
        print "Please enter input file"
        return -1
    
    d = []
    
    total, data = (0,0)
    nb = 0
    fd = open( argv[1], 'r' ) 
    for line in fd:
        l = line.split("\n")[0]
        d.append( l )
    fd.close()
    
    # fill the table of distances
    fillTable( d, distances )

    # Compute the cost of all the possible paths
    paths = computePaths( distances )

    bestpath = paths[0]
    bestcost = computeCost( bestpath, distances )
    for p in paths:
        c = computeCost( p, distances )
        if c > bestcost:
            bestpath = p
            bestcost = computeCost( bestpath, distances )

    print "Best:", bestcost, bestpath

    return bestcost
	
if __name__ == "__main__":
	count = main( sys.argv )
