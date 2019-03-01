#!/usr/bin/python3.5 

import MySQLdb as mysql 
import time 

'''
    1. MySQLdb.execute() 
        Returns the numbers of the affected rows by the query. 

    2. cursor.rowcount
        Return the number of total affectes rows. 

    3. cursor.fecthall() 
        Returns all affectes rows to programs. It is meanless to use .fetchall() that may give rise to slow or crash. 
    
    4. cursor.fetchone() 
        Return the first record that match the query as a result, which means that fetchone() returns exactly one row. If query affects no row, None is returned.
        It will automatically return rows by rows if it's called multiple times, which is like to readline() 

    5. cursor.fetchmany(<numbers of records to retrieve>) 
        Return blocks of results according to set limit. 

    ***Note*** 
        fetchall(), fetchone(), fetchmany() are iterable objects. 

''' 

def print_results( results_ ): 
    for i in results_: 
        print( i ) 

mydb = mysql.connect( host = 'localhost', user = 'root', 
                        passwd = 'Tv0912548857', db = 'students' ) 

statemnts = "Select * from studentstable;" 

cur_ = mydb.cursor() 

# 1. fetchall() 
command = cur_.execute(statemnts) 
results = cur_.fetchall() 
print('1. fetchall()') 
print_results(results) 
print('cursor.rowcount: ',cur_.rowcount) 
print( iter(results) ) # fetchall() is a iterable object.  

time.sleep(10) # take a break for 10 seconds.  

# 2. fetchone() 
command = cur_.execute(statemnts) 
results = cur_.fetchone() 
print('\n2. fetchone()') 
print(results) 
results = cur_.fetchone() 
print(results) # Different return compared to last call.  
results = cur_.fetchone() 
print(results) # Different return compared to last call.  

time.sleep(10) 

# 3. fetchmany() 
command = cur_.execute(statemnts) 
results = cur_.fetchmany(3) 
print('\n3. fetchmany()') 
print_results(results) 
