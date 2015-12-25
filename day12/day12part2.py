#!/usr/bin/env python

import sys
import json
import types
import unicodedata

def parseJSON( data ):
    nb = parseDict( data )
    return nb

def parseTable( data ):
    nb = 0
    for attr in data:
        if type( attr ) == types.DictionaryType:
            nb += parseDict( attr )
        elif type( attr ) == types.ListType:
            nb += parseTable( attr )
        elif type( attr ) == types.IntType:
            nb += attr
        else:
            if type( attr ) == types.UnicodeType:
                attr = unicodedata.normalize('NFKD', attr ).encode('ascii','ignore')
            nb += parseString( attr )
    return nb

def parseDict( data ):
    nb = 0
    for elem,attr in data.iteritems():
        if type( attr ) == types.DictionaryType:
            nb += parseDict( attr )
        elif type( attr ) == types.ListType:
            nb += parseTable( attr )
        elif type( attr ) == types.UnicodeType:
            s = unicodedata.normalize('NFKD', attr ).encode('ascii','ignore')
            if "red" == s:    # look for "red"
                return 0
            else:
                nb += parseString( s )
        elif type( attr ) == types.IntType:
            nb += attr
    return nb

def parseString( data ):
    nb = 0
    try:
        nb = int( data )
    except ValueError:
        pass
    return nb

            
def main( argv ):
    if 1 == len( argv ):
        print "Please enter input file"
        return -1
    
    nb = 0
    fd = open( argv[1], 'r' ) 
    jd = json.load( fd )
    fd.close()

    nb = parseJSON( jd )
    
    print nb
    return nb
	
if __name__ == "__main__":
	count = main( sys.argv )
