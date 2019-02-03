#!/usr/bin/python3.5 

import pandas as pd 
import datetime as dt 

# Timestamp objects 
ts = pd.Timestamp('2015-01-01') 
print( ts ) 
print( type(ts) ) 

# convert pandas Timestamp to datetime objects 
print( ">>  convert pandas Timestamp to datetime objects " ) 
ts = pd.to_datetime(ts) 
print(ts) 
print( type(ts) ) 


# convert datetime object to pandas Timestamp objects 
print( ">>   convert datetime object to pandas Timestamp objects " ) 
d = dt.datetime.now() 
d = pd.Timestamp(d) 
print(d) 
print(type(d)) 


# Use pd.date_range() to generate a range of Timestamp, like np.arange([],dtype='datetime64') 
print(">>   Use pd.date_range() to generate a range of Timestamp, like np.arange([],dtype='datetime64') " ) 
dti = pd.date_range('2011-01-23',freq = 'M', periods=14 ) 
print(dti) 
print(type(dti)) # a DatetimeIndex object  


# transform DatetimeIndex into arrays of datetime objects by .to_pydatetime() 
print(">>  transform DatetimeIndex into arrays of datetime objects by .to_pydatetime() ") 
pdti = dti.to_pydatetime() 
print(pdti) 
print(type(pdti)) # np.array 
# Inverse 
dti = pd.DatetimeIndex(pdti) 
print(dti) 
print(type(dti)) # a DatetimeIndex object  
# use .astype(pd.datetime) before transforming the numpy datetime64 to pd.DatetimeIndex 


# DatetimeIndex objects can be transformed from one time zone to another by tz_convert(). 
print(">>  DatetimeIndex objects can be transformed from one time zone to another by tz_convert()." ) 
dti = pd.date_range( '2011-02-10', freq='M', periods=30, tz='US/Eastern' ) 
print(dti) 
dti = dti.tz_convert("GMT") 
print(dti) 



