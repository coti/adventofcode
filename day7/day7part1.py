#!/usr/bin/env python

import sys
import types

def getValue( a, circuit ):
        try:
                va = int( a )
        except:
                if a not in circuit.keys():
                        return -1
                va = circuit[a]
        return va

def inputsignal( value, wire, circuit ):
	va = getValue( value, circuit )
        if va == -1:
                return -1
	circuit[wire] = va
	return

def bitwisecomplement( inwire, outwire, circuit ):
	va = getValue( inwire, circuit )
	if va == -1:
		return -1
	circuit[outwire] = (~ va) & 0xffff
	return

def bitwiseor( a, b, c, circuit ):
	va = getValue( a, circuit )
	vb = getValue( b, circuit )
	if va == -1 or vb == -1:
		return -1
	circuit[c] = ( va | vb )
	return

def bitwiseand( a, b, c, circuit ):
	va = getValue( a, circuit )
        vb = getValue( b, circuit )
        if va == -1 or vb == -1:
                return -1
        circuit[c] = ( va & vb )
        return

def leftshift( a, n, z, circuit ):
	va = getValue( a, circuit )
        if va == -1 :
                return -1
	circuit[z] = ( va << n ) & 0x0ffff
	return

def rightshift( a, n, z, circuit ):
        va = getValue( a, circuit )
        if va == -1 :
                return -1
        circuit[z] = ( va >> n )
	return

def handleInstruction( s, circuit ):
	inp,outp = s.split(  ' -> ' )
	inp = inp.split( ' ' )
	outp = outp.split( "\n" )[0]

	if len( inp ) == 1: # case 123 -> x or a -> b
		rc = inputsignal( inp[0], outp, circuit )
	elif len( inp ) == 2:
		if inp[0] == 'NOT': # case NOT e -> f
			rc = bitwisecomplement( inp[1], outp, circuit )
		else:
			print "Unknown instruction:", ' '.joint( inp )
	elif len( inp ) == 3:
		if inp[1] == "AND": #case x AND y -> z
			rc = bitwiseand( inp[0], inp[2], outp, circuit )
		elif inp[1] == "OR": #case x OR y -> z
			rc = bitwiseor( inp[0], inp[2], outp, circuit )
		elif inp[1] == "LSHIFT": #cast a LSHIFT n -> b
			rc = leftshift( inp[0], int( inp[2] ), outp, circuit )
                elif inp[1] == "RSHIFT": #cast a RSHIFT n -> b
			rc = rightshift( inp[0], int( inp[2] ), outp, circuit )
		else:
			print "Unknown instruction:", ' '.joint( inp )
	else:
		print "Unknown instruction:", ' '.joint( inp )
	return rc

def main( argv ):
	circuit = {}
	postponed = []

	if 1 == len( argv ):
		print "Please enter input file"
		return -1

	fd = open( argv[1], 'r' ) 
	for line in fd:
		rc = handleInstruction( line, circuit )
		if -1 == rc:
			postponed.append( line )
	fd.close()

	while len( postponed ) > 0:
		n = []
		for line in postponed:
			rc = handleInstruction( line, circuit )
                	if -1 == rc:
                        	n.append( line )
		postponed = n

	nb = circuit['a']
	print "Signal on wire a:", nb
	return nb
	
if __name__ == "__main__":
	count = main( sys.argv )
