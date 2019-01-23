# Question 9
LINES = [] #Declare a list to place every line of input

 
#If INPUT has value then append the value to Lines and CONTINUE, or break. 

while True:
	INPUT = input(">>")
	if INPUT:		
		LINES.append( INPUT.upper() )
	else:
		break

for sentence in LINES:
	print( sentence )
