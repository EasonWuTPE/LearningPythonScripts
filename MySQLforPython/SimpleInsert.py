#!/usr/bin/python3.5 

import MySQLdb as mysql 

mydb = mysql.connect( host='localhost', user='root', passwd = '***', db='students' ) 
cur = mydb.cursor() 

table_name = 'studentstable' 
column_name = 'name, school_id, height' 
val1 = "\"Easy\", \"1021213\", \"193\"" 

''' INSERT INTO <table>(<columns>) VALUES (<"values">); '''
'''as same as REPLACE INTO <table> SET("<columns>" = "<values>"); '''
cur.execute("insert into %s (%s) values (%s);"%(table_name,column_name,val1))) # .execute("query") would return the numbers of row selected from table, but .execute("insert") return nothing. We usually assign a variable to return data.  
print( "Insert sucessully!\n" ) 

'''NOTE'''
''' INSERT INTO <target table>(<target columns>) SELECT <source columns> FROM <source table> (Condition); ''' 
'''     Insert values from different tables without drawing that tables into Python or setting variables. '''  
''' INSERT DELAYED INTO <table>(<columns>) VALUES(<"values">); ''' 
'''     insert data to table until no query to the table. ''' 
mydb.commit() 
mydb.close() 


