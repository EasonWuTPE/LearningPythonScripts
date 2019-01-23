#!/usr/bin/python3

# Factoria of a number.

def fact( x ):
	if x == 1:
		return 1
	return x * fact( x-1 )

x = int( input( ">>" ) )

print( fact( x ) )
