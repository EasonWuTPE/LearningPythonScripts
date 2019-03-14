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
# It returns the dict for first which the 'dest' arg in .add_option is the key and value from command-line is the value, 
#   and returns the list for the second which put the rest of the values from command-line. 
opt, args = opt.parse_args()  

# Whatever value is given in the 'dest' of .add_option becomes  an attribute of the OptionParser. 
first_arg = opt.first_arg 
second_arg = opt.second_arg 
third_arg = opt.third_arg 

# opt is the dictionart that record the key and correspond value, which 'dest' is key and the value is arguments received from command-line. 
print( 'opt:', opt ) 
# args received the rest of values from command-line 
print( 'args:', args ) 
# You can try $ ./example_Received_Arguments_from_Command_by_optparse -f 'A' -s 'B' -t 'C' 'The' 'Rest' 'of' 'Command' 'Line' 

print( "All arg received from command-line is %s, %s, %s." %( first_arg, second_arg, third_arg ) ) 



