#!/usr/bin/python3.5 

import optparse 

''' 
    This scripts will record the arguments received from command-line by the module "optparse", 
''' 

# Initialize 
opt = optparse.OptionParser() 
# Add option 
opt.add_option( '-f','--first',action='store',type='string',dest='first_arg' ) 
opt.add_option( '-s','--second',action='store',type='string',dest='second_arg' ) 
opt.add_option( '-t','--third',action='store',type='string',dest='third_arg' ) 
# Compile after adding option 
opt, args = opt.parse_args() 
# Whatever value is given in the 'dest' of .add_option becomes  an attribute of the OptionParser. 
first_arg = opt.first_arg 
second_arg = opt.second_arg 
third_arg = opt.third_arg 

print( "All arg received from command-line is %s, %s, %s." %( first_arg, second_arg, third_arg ) ) 



