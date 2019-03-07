#!/usr/bin/python3.5 

import MySQLdb as mysql 

# DATABASES 

''' 
    1. Create Database: 

        >> CREATE DATABASE [IF NOT EXISTS]  <database name>; 

        On Unix-base system, CREATE database is case-sensitivity by default. 
        But Windows and MacOS "may" not be. 

    2. Create specification: 
        2.1 character set (by default): It is a set of symbols and encodings used to represent and store the info held in a database.
        
              >>  CREATE DATABASE [IF NOT EXISTS] <database name> [CHARSET = <encoding(e.g. utf8)>]; 

              >>  CREATE DATABASE [IF NOT EXISTS] <database name> [CHARACTER SET = <encoding(e.g. utf8)>]; 

        2.2 collation used: It is a collation system of rules that MySQL uses to work with the databases for purpose of comparsion and matching. 
                
              >>  CREATE DATABASE [IF NOT EXISTS] <database name> [CHARSET = <encoding(e.g. utf8)>] [COLLATE = <rule(e.g. utf8_general_ci)>]; 

              >>  CREATE DATABASE [IF NOT EXISTS] <database name> [CHARACTER SET = <encoding(e.g. utf8)>] [COLLATE = <rule(e.g. utf8_general_ci)>]; 
            
            *** Apply the e.g. to syntax, it seems that the collation definition is not necessary as every character set has its own set of collation available for it. 
        
        *** Finding the CHARSET and COLLATE is MySQL shell $ >> show character set; 
        *** Not all collation can be used with every character set. 

'''

''' 
    1. Drop databases: 

        >> DROP DATABASE [IF EXISTS] <database name>; 
        *** Note that DROP statement not only deletes the structure of the database setup by CREATE statement but also irrecoverably drop all of the databases.

    2. Prevent access after drop databases: 
        To prevent someone from creating the same database name after dropping, one must revoke user privileges on database. 

        >> REVOKE <privileges> ON <database.table> FROM <users>; 

''' 

# TABLES 
''' 
    1. Create tables require definition at least one column. 

        >> CREATE TABLE [IF NOT EXISTX] <table name> ( '<col name>' < column specification >, ... , [primary key(col name)] ); 
        
        ***Notes: 
        >> CREATE TABLE abc ( col1 varchar(30) NOT NULL ); # create table abc with one colum col1 in trauncated to 30 characters with No NULL Values. If exixts null value, it raise error.  

        >> CREATE TABLE abc ( col1 varchar(30) NOT NULL DEFAULT ' '); # create table abc with one colum col1 in trauncated to 30 characters. The value is ' ' defaultly when user doen't input any value.  

    2. Create tables temporary: 
        
        >> CREATE TEMPORARY TABLE [IF NOT EXISTX] <table name> ( '<col name>' < column specification >, ... , [primary key(col name)] ); 
        Note that temporary tables are only visible to the user session that create it. 
        When this kind of tables are created, MySQL will report that "0 rows has been affected" and show nothing in the list. 
''' 
''' 
    1. Drop tables: just like drop database.  

        >> DROP [TEMPORARY] TABLE [IF EXISTS] <database name>; 
        *** Note that DROP statement not only deletes the structure of the database setup by CREATE statement but also irrecoverably drop all of the databases.

    2. Prevent access after drop table: 
        To prevent someone from creating the same database name after dropping, one must revoke user privileges on database. 

        >> REVOKE <privileges> ON <database.table> FROM <users>; 

''' 
    
mydb = mysql.connect('localhost','root','Tv0912548857') 
cur_ = mydb.cursor() 
db_name = 'students' 
statements1 = "CREATE DATABASE IF NOT EXISTS %s" 
command = cur_.execute(statements1%(db_name)) # reutrn something. 
print(command) 



