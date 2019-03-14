#!/usr/bin/python3.5 

import sys 

''' 
    This scripts will record the arguments received from command-line by the module "sys", 
''' 
# The sys.argv[0] is the program itself. 
_from = sys.argv[1] 
_to = sys.argv[2] 
name = sys.argv[3] 

print("The arg recieved from command-line is: %s, %s and %s."%(_from,_to,name) ) 


