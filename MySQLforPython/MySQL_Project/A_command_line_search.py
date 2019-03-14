#!/usr/bin/python3.5 

import sys # used for receive a command-line argument by this module.  
import optparse # used for parse the received arg from comman-line. 
import MySQLdb as mysql 

''' Arguments Received from Command-Line by sys -> this may be error-prone.  

    table = sys.argv[1] 
    column = sys.argv[2] 
    term = sys.argv[3] 

''' 
''' Arguments Received from Command-Line by optparse 

    The numbers of arg received from command-line: 
        0: the command-line itself 
        1: the flag -t 
        2: the table name 
        3: the flag -c 
        4: the column name
        5: the flag -q 
        6: the searching string for query. 

    --> 7 arguments to be recieved. 
''' 
# INITIALIZE
opt = optparse.OptionParser()  
# ADD OPTIONS 
opt.add_option( '-t','--table',action='store', type='string',dest='table' ) # add an option for the table.
opt.add_option( '-c','--column',action='store', type='string',dest='column' ) # add an option for the column. 
opt.add_option( '-q','--query',action='store', type='string',dest='term' ) # add an option for the query. 
# COMPILE AFTER ADDING OPTIONS 
opt, args = opt.parse_args() # compile them after add options. 
# Whatever value is given in the 'dest' of .add_option becomes  an attribute of the OptionParser. 
table = opt.table 
column = opt.column 
term = opt.term 



''' MySQLdb Module ''' 
mydb = mysql.connect( host='localhost',user='root', 
                        passwd='***', db='world' ) 
cur = mydb.cursor() 

# Variables 
#table = "city" 
#column = 'Name' 
#term = '%s' 
statement = "SELECT * FROM %s WHERE %s LIKE '%s'"%(table,column,term) 

# Execute 
command = cur.execute(statement) 
results = cur.fetchall() 

#print(results[:10]) 

results_list = [] # used to reorange the results from fetchall() 
for i in results:
    results_list.append( [i[0],i[1]] ) 

#print(results_list[:10]) 

for val in range(0,len(results)): 
    print( val+1, results_list[val][1] ) 



