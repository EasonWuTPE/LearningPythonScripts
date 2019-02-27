#!/usr/bin/python3.5 

import MySQLdb as mysql 

mydb = mysql.connect( host='localhost', user='root', 
                    passwd = '***', db = "students" ) 

cur_ = mydb.cursor() 

tables = "studentstable" 
command = cur_.execute( "select * from %s;"%tables ) # returns the numbers of the table.
results = cur_.fetchall() 
#print(command) 
#print(results) 


def show(results): 
    for i in range(0,len(results)): 
        print("%d %s"%(i+1,list(results[i])))
    print('\n',end='') 


# Query Dynamically 
input_query = "x%z"  
'''
    "%x" : a values that end with letter x 
    "x%" : a values that begin with letter x 
    "x%z%": a values that begin with letter x and contains at least one instance of the letter l 
    "x_z%" : a values that begin with letter x and whose third letter is z 
    "_____" : a five letter value 
    "__%" : a values with least two characters 
'''
command = cur_.execute("select * from %s where name like '%s';"%(tables,input_query) ) 
results = cur_.fetchall() 
show(results) 
command = cur_.execute("select * from %s where name not like '%s';"%(tables,input_query) ) 
results = cur_.fetchall() 
show(results) 
command = cur_.execute("select * from %s where name = '%s';"%(tables,input_query) ) 
results = cur_.fetchall() 
show(results) 
command = cur_.execute("select * from %s where name <> '%s';"%(tables,input_query) ) 
results = cur_.fetchall() 
show(results) 

mydb.close() 

