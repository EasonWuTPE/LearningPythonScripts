#!/usr/bin/python3.5
# Question 10

sentence = input( ">> " )
string = list( set( sentence.split() ) )
string.sort()

print( ' '.join( string ) )


