#!/usr/bin/python3.5 

import MySQLdb as mysql 

x = '' 

if x == '': 
    raise mysql.Error("Error Happens") # error messeges customized.  

if x == '': 
    raise mysql.Error 


if x == '': 
    raise mysql.Warning 

if x == '': 
    raise mysql.Warning("Warning alart") 


'''         Different types of exception            ''' 
'''
        1. DataError
            Errors are raised with processed data. 
        2. IntegrityError 
        3. InternalError 
            e.g. invalid cursor, transaction is out of sync. 
        4. NotSupportedError 
        5. OperationalError 
        6. ProgrammingError 

    Each of types of exception can be caught with the DatabaseError type. 

        1. Catch one exception: 

            try: 
                statements 
            except MySQLdb.<error type> as e: 
                raise e 

        2. Catch different exceptions: 

            try: 
                statements 
            except MySQLdb.<error type I> as e: 
                raise e 
            except MySQLdb.<error type II> as e: 
                raise e 

        3. Combine exceptions: 

            try: 
                statements 
            except (MySQLdb.<error type>, MySQLdb.<error type>) as e: 
                raise e 

''' 


