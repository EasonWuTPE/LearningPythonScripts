#!/usr/bin/python3.5 

import MySQLdb as mysql 

# usually specify the database here ( or optional ). New connection is necessary if new database is specified.  
mydb = mysql.connect( host="localhost", user="root",
                        passwd = "***", db="students" ) 
cur = mydb.cursor() 

''' 
    results_variable = cursor_handle.execute("MySQL statements") 
        
        .execute() will return an object. 
''' 
#cursor.execute('insert into studentstable (name,school_id,height) values (\"ese\","1212234\",\"157\");') 
#mydb.commit() 
#mydb.close() 

command = cur.execute("select * from studentstable;") # cursor.execute("Query statement") returns the number of the row that selected from table, but "Insert statement" return nothing. 
results = cur.fetchall() 
print(command) 
print(results) 

print( "\nThe students table is: " ) 
for i in results: 
    print(i[0],i[1],i[2],i[3]) 


command = cur.execute("select * from studentstable where height > 160;")  
results = cur.fetchall() 
print( "\nThe students table is: " ) 
for i in results: 
    print(i[0],i[1],i[2],i[3]) 

val = 160 
command = cur.execute("select * from studentstable where height > %d;"%(val))  
results = cur.fetchall() 
print( "\nThe students table is: " ) 
print(command) 
for i in results: 
    print(i[0],i[1],i[2],i[3]) 
'''
The execute() method is simply passing the MySQL statement as a string to _mysql, 
    which in turn passes it to the C database API, 
    which in turn passes it to MySQL. 
'''



