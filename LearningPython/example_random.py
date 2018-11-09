'''
The examples of module random
'''

import random as rd # Must import module before using it

print( "Choose an integer in [2,100] at random is: {}".format( rd.randint( 2, 100) ) )
print( "Randomly choose a number [0, 1.0) : {} ".format( rd.random() ) )
print( "Random choose from (0, 3, 6, ..., 99) :{}.".format( rd.randrange(0,100,3) ) )
rd.seed() # Initialize the seed, defaultly seed == time.

# Choose an item from list at random
x1 = [ "BMW", "Lamborgini", "Mazda", "Mecedes", "Porsche"]
print( "Choose a manufacture randomly: {}".format( rd.choice( x1 ) ) )

'''
    Shuffle a list ( only list )
 ****random.shuffle() only shuffle the list in place and return "NONE", 
	so it cannot be assigned to other variables.****
'''
x2 = ["Porsche", "Mecedes-Benz", "BMW", "Lamborghini", "Audi"]
print( "list before shufflng: {}".format( x2 ) )
rd.shuffle(x2)
print( "list after shuffling: {}".format( x2 ) ) 
