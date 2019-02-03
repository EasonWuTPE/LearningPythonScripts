#!/usr/bin/python3.5 

# Deal with time and datetime problems 
 
import datetime as dt 


# Current date and time 
print( "Now is:", dt.datetime.now() ) 
today_ = dt.datetime.today() 
print( "Another way: ", today_ ) 
print( "The type is:",type(today_) ) # datetime object  
print( "Week day is:",dt.datetime.now().weekday() )
print( "Week day is:",dt.datetime.today().weekday() )


# Create datetime 
d_ = dt.datetime( 2019,1,1,10,5,30,00 ) 
print("d_:",d_) 
print('type: ', type(d_) ) # Type is datetime object 

# Others 
print( d_.month ) # 1 
print( d_.year ) # 1
print( d_.hour ) # 10
print( d_.weekday() ) # Tuesday = 1  

