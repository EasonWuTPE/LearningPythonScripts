#!/usr/bin/python3.5 

import MySQLdb as mysql 
import optparse 
import getpass 
from prettytable import PrettyTable 
import smtplib 

''' Define class ''' 
class Form_MySQL_Statement(): 

    ''' This class object is used to form a complete statement of MySQL. ''' 

    def __init__(self): 
        self.Statement = [] 

    def type(self,kind): 
        ''' The type of statement: SELECT, INSERT, UPDATE ''' 
        self.type = kind  

    def form(self,table,column,info): 
        ''' Form the MySQL statement by the type of statement. ''' 

        # Form the value 
        data = info.split(',') 
        value = "'"+data[0] 
        for i in range(1,len(data)): 
            value = value + "','"+data[i] 
        value += "'" 

        # Form the complete statement by multiple class  
        full_statement_dict = { 
                                'select':"SELECT * FROM %s WHERE %s=%s"%(table,column,value), 
                                'insert':"INSERT %s(%s) VALUES(%s)"%(table,column,value), 
                                'update':"UPDATE %s SET %s=%s WHERE %s=%s"%(table,column,data[0],column,data[0]) 
                              } 

        return full_statement_dict[self.type] 

    def execute_statement(self, statement, table, cursor ): 
        ''' Execute the result of Form_MySQL_Statement.form() ''' 
        while True: 
            try: 
                print("Try SQL statement: '%s'..."%(statement)) 

                if self.type == 'select': 
                    self.getColumnSelect(cursor,table)  
                    affected_row = cursor.execute(statement) 
                    self.getResultSelect(cursor,affected_row) 
                else: 
                    affected_row = cursor.execute(statement) 


                print( "Your statement: '%s' has been executed!!"%(statement) ) 
                return  "Your statement: '%s' has been executed!!"%(statement) 
            # OperationalError
            except mysql.OperationalError as e: 
                print("\nOperationalError!!\n") 
                raise e 
            # DataError, ProgrammingError
            except (mysql.DataError,mysql.ProgrammingError) as e:
                print("\nDataError or ProgrammingError!!\n") 
                raise e 
            except mysql.IntegrityError as e: 
                print("\nIntegrityError!!\n") 
                raise e 
            # InternalError, NotSupportError
            except (mysql.InternalError, mysql.NotSupportedError) as e: 
                print("\nInternalError or NotSupportedError!!\n") 
                raise e 
            except mysql.Warning: 
                pass 

    def getColumnSelect(self,cur_,table): 
        statement = "DESCRIBE %s"%(table) 
        num = cur_.execute(statement) 
        columns_results = cur_.fetchall() 
        print("DEBUG:",columns_results) 
        to_list = [] 
        for i in range(len(columns_results)): 
            to_list.append(columns_results[i][0]) 
        self.to_table = PrettyTable(to_list)

    def getResultSelect(self,cur_, row): 
        results_of_select = cur_.fetchall() 
        to_list = [] 
        for k in range(row): 
            for i in range(len(results_of_select[k])): 
                to_list.append(results_of_select[k][i]) 
        self.to_table.add_row(to_list) 
        print(self.to_table) 

''' Other functions ''' 
def check_valid_input( bechecked, name ): 
    while bechecked == '' or bechecked == None: 
        bechecked = input("Invalid %s! You need to input the %s. Try again! >> $ "%(name,name)) 

    return bechecked 

def Connection( database, password ): 
    
    try: 
        mydb = mysql.connect( 'localhost', 'root', password, db=database ) 
        cur = mydb.cursor() 
        print("\nConnection Success!!\n") 
        return cur 
    except mysql.Error:
        print("\nSomething Wrong! Please ensure that you have input the database exist on local system.\n") 
        raise mysql.Error 
    except mysql.Warning: 
        pass 

def sendmail( msg, recipient ): 
    ''' 
    fromaddr = "tvjs168@gmail.com" 
    toaddr = recipient+"@gmail.com" 
    msg = 
    ''' 
    pass 

    

''' Main function ''' 
def main(): 
    
    # Received arguments from command-line 
    opt = optparse.OptionParser() 
    opt.add_option('-i','--insert',action='store_true',help='flag for requesing insert.',dest='insert') 
    opt.add_option('-u','--update',action='store_true',help='flag for requesing update.',dest='update') 
    opt.add_option('-s','--select',action='store_true',help='flag for requesing select.',dest='select') 
    opt.add_option('-d','--database',action='store',type='string',help='the name of database.',dest='database') 
    opt.add_option('-t','--table',action='store',type='string',help='the name of table.',dest='table') 
    opt.add_option('-c','--columns',action='store',type='string',help='the name of columns.',dest='columns') 
    opt.add_option('-v','--values',action='store',type='string',help='value to be stored.',dest='values') 
    opt.add_option('-p','--password',action='store',type='string',help='password to login in.',dest='password') 
    opt, args = opt.parse_args() 

    # Only one kind of MySQL statement type is allowed. If more than one, the priority is SELECT > UPDATE > INSERT 
    if opt.select is True: 
        statement_type = 'select' 
    elif opt.update is True: 
        statement_type = 'update' 
    elif opt.insert is True: 
        statement_type = 'insert'  

    # check the valid of strings 
    database = check_valid_input(opt.database, 'database') 
    table = check_valid_input(opt.table, 'table') 
    columns = check_valid_input(opt.columns, 'columns') 
    values = check_valid_input(opt.values,'values') 
    password = check_valid_input(opt.password,'password') 

    # Connection 
    connection_cursor = Connection( database, password ) 

    # Action 
    request = Form_MySQL_Statement() 
    try:
        request.type(statement_type) 
        phrase = request.form(table,columns,values) 
        results = request.execute_statement(phrase, table, connection_cursor ) 
        print("Results: %s\n"%(results)) 
        
        connection_cursor.close() 

    except mysql.MySQLError as e: 
        print("The values you entered are not valid. Please check it again!") 
        raise mysql.Error 
    except mysql.Warning: 
        pass 


if __name__ == '__main__': 
    main() 



