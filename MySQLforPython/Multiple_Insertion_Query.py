#!/usr/bin/python3.5 

# Multiple insertion to MySQL 

import MySQLdb as mysql 

''' 
    cursor.execute() is too slow to insert multiple data. 

    cursor.executemany() is more efficient and typically faster than iteration. 

    Basic Syntax: 

        cursor.executemany(<MySQL statements>,<arguements(a sequence)>) 
            Both arguements are required, otherwise, a TypeError will be thrown by Python. 
            < MySQL statements >: INSERT, SELECT ... so on. 
            < arguements >: A suquence containing parameters to use within Python. 

''' 

mydb = mysql.connect( host='localhost',user='root',passwd='Tv0912548857',db='students' ) 
cur_ = mydb.cursor() 

data = [ ["apple",1254364,176],["cat",2317453,192] ] 
#data = [ ("apple",1254364,176),("cat",2317453,192) ] 
#statements1 = "insert into studentstable( name, school_id,height) values(%s,%s,%s);" 
#cur_.executemany( statements1, data ) 
#cur_.close() 

statements2 = "select * from studentstable where name=(%s,%s);" 
command = cur_.executemany( statements2, ('xyz','eee') ) 

mydb.commit() 
mydb.close() 



