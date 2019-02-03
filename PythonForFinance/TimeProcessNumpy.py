#!/usr/bin/python3.5 

import numpy as np 
import datetime as dt 

print( ">> Some " ) 
ndt = np.datetime64('2018-01-31') 
print( ndt ) 
print( type(ndt) ) 
print( str(ndt) ) 

ndt_str = np.datetime_as_string(ndt) 
print(ndt_str) 
print(type(ndt_str)) 

print( np.datetime_data(ndt) ) 


# >> From datetime object to np.datetime64. 
print( ">> From datetime to np.datetime64 object." ) 
d = dt.datetime.now() 
d_n = np.datetime64(d)
print(d_n) 
print(type(d_n)) 


# >> From np.datetime64 to datetime object. 
print( ">> From np.datetime64 to datetime object." ) 
ndt.astype(dt.datetime) 
print( ndt ) 
print( type(ndt) ) 


# Define a datetime64 datatpye in np.array 
# dtype = 'datetime64[frequency]' 
print(">>  Define a datetime64 datatpye in np.array ") 
time_arr = np.array( ['2018-01-01','2018-01-02','2018-01-03'], dtype='datetime64' ) 
print( time_arr ) 
time_arr = np.array(['2018-01-01','2018-01-02','2018-01-03'], dtype='datetime64[s]') 
print( time_arr ) 
time_arr = np.array( ['2018-01-01','2018-01-02','2018-01-03'], dtype='datetime64[M]') 
print( time_arr ) 

# Use np.arange to generate the range of day 
# dtype = 'datetime64[frequency]' 
print(">>   Use np.range to generate the range of day ")
time_arange = np.arange('2018-01-01','2018-01-15',dtype='datetime64') 
print(time_arange) 
time_arange = np.arange('2018-01-01','2018-01-15',dtype='datetime64[s]') 
print(time_arange) 
time_arange = np.arange('2018-01-01','2018-01-15',dtype='datetime64[W]') 
print(time_arange) 
time_arange = np.arange('2018-01-01','2018-10-15',dtype='datetime64[M]') 
print(time_arange) 
time_arange = np.arange('2015-01-01','2019-10-15',dtype='datetime64[Y]') 
print(time_arange) 

