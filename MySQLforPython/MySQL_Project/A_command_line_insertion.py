#!/usr/bin/python3.5 

import optparse 
import getpass # Used for logining accounts   
import MySQLdb as mysql 
from prettytable import PrettyTable 

# define some functions 
def check_databases( bechecked ): 
    while bechecked == '' or bechecked == None: 
        print( "Unkown databases, try again !" ) 
        bechecked = input(">>") 
    return bechecked 

def check_passwd( bechecked ): 
    while bechecked == '' or bechecked == None: 
        print( "Unkown password, try again !" ) 
        bechecked = getpass.getpass() 
    return bechecked 

def check_usr( bechecked ): 
    while bechecked == '' or bechecked == None: 
        print( "Unkown user, try again !" ) 
        bechecked = getpass.getuser() 
    return bechecked 

def check_valid_tables( bechecked, bechecked_list ): 
    while True: 
        if bechecked > len(bechecked_list):  
            print("Choice out of tables") 
            bechecked = int(input("Try again>>"))  
        else: 
            break 
    return bechecked 

def is_describe_tables( tables, cursor_objects, print_describe ): 
    describe_table_statement = "describe %s"%(tables) 
    command = cursor_objects.execute(describe_table_statement) 
    results = cursor_objects.fetchall() 

    # Use PrettyTable() to format the tables with column name. 
    table_def = PrettyTable( ["Feild","Type","Null","Key","Default","Extra"] ) 

    for i in range(len(results)): 
        # Add values row by row 
        table_def.add_row( [ results[i][0], results[i][1], results[i][2], results[i][3], results[i][4], results[i][5] ] ) 

    # Print out the results. 
    if print_describe == 'y' or print_describe == 'Y': 
        print( table_def ) 
    return results 


def getInsertStatement( describe_chosen_table_, the_chosen_table_name_ ): 
    cols = [] 
    vals = [] 
    for i in range(len(describe_chosen_table_)): 
        values = input("Value to input column %s: "%(describe_chosen_table_[i][0]) ) 
        cols.append(describe_chosen_table_[i][0]) 
        vals.append("'"+values+"'") 
    cols = ','.join(cols) 
    vals = ','.join(vals) 
    print( "\n\nThe insert statements is:\nINSERT INTO %s(%s) VALUES(%s)"%(the_chosen_table_name_, cols, vals ) ) 
    return "INSERT INTO %s(%s) VALUES(%s)"%(the_chosen_table_name_, cols, vals) 


# Define main function 
def main(): 

    # Initialization 
    opt = optparse.OptionParser() 
    # Add options 
    opt.add_option( '-d', '--database', action='store', type='string', dest='database' ) 
    opt.add_option( '-p', '--passwd', action='store', type='string', dest='passwd' ) 
    opt.add_option( '-u', '--user', action='store', type='string', dest='user' ) 
    opt, args = opt.parse_args() 

    database = check_databases(opt.database) 
    passwd = check_passwd(opt.passwd) 
    user = check_usr(opt.user) 
    #print( database, passwd, user ) 

    # Try to connect to MySQL 
    try: 
        mydb = mysql.connect(host='localhost',user = user, passwd = passwd, db = database ) 
        cur = mydb.cursor() 
        quit = 1 # 1, if connect sucessfully. 
        print("Connection Sucessfully") 
    except: 
        print("Logging information error!") 
        quit = 0 # 0, if connect failure. 
        exit(0) # exit the program 

    # Show tables 
    if quit == 1: 
        gets_tables_statements = "show tables;"
        affected_rows = cur.execute(gets_tables_statements) 
        tables = cur.fetchall()  
        
        # Show all tables 
        print( "\nThe tables shown below." ) 
        tables_list = [] # To record the tables of database 
        for tables_ in range(0,len(tables)): 
            tables_list.append(tables[tables_][0]) 
            print( tables_+1, tables_list[tables_] ) 
        # check user input is valid or not. 
        num_of_table = check_valid_tables( int(input("\nEnter the numbers that you want to insert data.\n>> ")), tables_list ) 
        the_chosen_table_name = tables_list[num_of_table-1] 

    # Describe tables or not? 
    choice = input("\nDo you want to show detail of that table? [y/n]" ) 
    describe_chosen_table = is_describe_tables( tables_list[num_of_table-1], cur, choice ) 

    # Insert the values to table 
    print( "\n\nThe value that you want to insert into tables %s"%(the_chosen_table_name) ) 
    insert_statements = getInsertStatement( describe_chosen_table, the_chosen_table_name ) 
    cur.execute(insert_statements) 

    # Close 
    #cur.close() 
    #mydb.commit() 
    #mydb.close() 


if __name__ == '__main__':
    main() 

    

