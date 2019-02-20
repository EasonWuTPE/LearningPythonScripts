#!/usr/bin/python3.5 

''' Four stages of database communication ''' 
'''
    1. create a connection  object -> connection 
    2. create a cursor object -> mark your place and issue commands to the computer. 
    3. interact with database -> issue commands  
    4. close the connection 
'''
import _mysql 
import MySQLdb as mysql 

'''    1. create a connection  object    ''' 
'''
        name = mysql.connect( host="[hostname]", user="[username]", 
                              passwd="[password]", db="[database name]" ) 
'''
mydb = mysql.connect( host="localhost", user="root", 
                      passwd="***", db="mydb" ) 

'''    2. create a cursor object    ''' 
'''
        cursor_name = connect_name.cursor()  
'''
cursor = mydb.cursor() 


'''    3. interact with database    ''' 
'''
            Interact with the database by MySQL codes. 
'''
cursor.execute("insert into mytable (username,email) values (\"xyz\",\"xyz@example.com\");") 



'''    4. close the connection      ''' 
'''
        Whether to close() depends on what actions you have performed and MySQL's auto-commit. 
        autocommit is switched on by default. If not, you have to commit any change you have made. 
''' 
mydb.commit() 
''' Once all changes are commited, close the database. ''' 
mydb.close() 



