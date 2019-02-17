#!/usr/bin/python3.5 

import MySQLdb as mysql 

mydb1 = mysql.connect( host = "localhost", user="root", passwd="Tv0912548857" ) 

cursor = mydb1.cursor() 

cursor.execute("create database if not exists students;") 
cursor.execute("use students") 
cursor.execute(
            "create table if not exists studentstable(id int unsigned not null auto_increment,name varchar(30) not null,school_id int unsigned not null,height int unsigned not null, primary key (id) );" 
                ) 
cursor.execute(
        "insert into studentstable (name,school_id,height) values (\"xyz\",\"1232121\",\"174\");"
                ) 

mydb1.commit() 
mydb1.close() 



