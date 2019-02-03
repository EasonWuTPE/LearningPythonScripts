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
print(">>  Create datetime") 
d_ = dt.datetime( 2019,1,1,10,5,30,00 ) 
print("d_:",d_) 
print('type: ', type(d_) ) # Type is datetime object 
t_ = dt.datetime.time(d_) 
t1_ = dt.datetime.weekday(d_) 
print( "t_: ",t_ , ', t1_:',t1_) 

# Others 
print( d_.month ) # 1 
print( d_.year ) # 1
print( d_.hour ) # 10
print( d_.weekday ) # returns a < built-in method datetime.datetime object at memory.> 
print( d_.weekday() ) # Tuesday = 1  

# To original 
print(">>  To original " )
O = d_.toordinal() 
print( O ) 
# From orignal 
print(">>  From original, may lose information. " )
print( dt.datetime.fromordinal(O) ) # This may lose some information.  

# Separate the specific information 
print(">> Separate the specific information.")  
dd = dt.datetime.date(d_) 
print(dd) 
tt = dt.datetime.time(d_) 
print(tt) 

# timedelta 
delta = d_ - dt.datetime.now() 
print( ">> timedelta " ) 
print( 'delta: ', delta ) 
print( type(delta) ) 
print( delta.days ) 
print( delta.seconds ) 
print( delta.microseconds ) 
print( delta.total_seconds() ) 

# Transform a datetime object into different representation 
print( ">>  Transform a datetime object into different representation" )  
print( d_.isoformat() ) 
print( type(d_.isoformat()) ) 
print( d_.strftime("%A, %d. %B %Y %I:%M%p") ) # convert from datetime object to string by specific formation. 
print( type(d_.strftime("%A, %d. %B %Y %I:%M%p")) ) 
print( dt.datetime.strptime('2017-03-12', '%Y-%m-%d') ) # convert from string to datetime object by specific formation. 
print( type(dt.datetime.strptime('2017-03-12', '%Y-%m-%d')) )
print( str(dt.datetime.strptime('2017-03-12', '%Y-%m-%d')) )
print( type(str(dt.datetime.strptime('2017-03-12', '%Y-%m-%d'))) )

# utcnow() 
print('>>  utcnow() ') 
print( dt.datetime.now() ) 
print( dt.datetime.utcnow() ) 
print( dt.datetime.now() - dt.datetime.utcnow() )  

# tzinfo?? pytz module?? 



