#!/usr/bin/python3.5 

import MySQLdb as mysql 
import cgi # A module imported to use CGI 
import cgitb # A module imported for giving us helpful error messages if we need to debug the program. 
import optparse 
''' 
form = cgi.FieldStorage() 
name = form.getvalue('firstname') # cgi.FieldStorage.getvalue() used for accessing CGI input. 
address = form.getvalue('surname') 
phone = form.getvalue('phoneno') 
''' 
''' After receiving and processing the inputs from CGI, the ouput of one's program is sent to the web client throught thr server.''' 
''' 
    CGI cannot pass data from one page to another. 
    The alternative would be to pass information through flags, but CGI doesn't support a secure way to do this. 
    Any values that persist from one page to another would have to be embedded in the code, which is viewable and can be spoofed by 
    any user who knows that information. 
''' 
''' 
    Using PHP substitute for CGI. 
        Using CGI, the program to be called is always shown in the HTML source code. 
        One therefore tips one's hand and show that the system processing the data in Python. 
        By using PHP to hand the data off to Python, 
            one introduces a hidden layer of complexity that makes cracking the system more difficult. 
''' 

# HTML Class 
class HTMLPage(): 
    def __init__(self): 
        self.statement = [] 

    def message(self, msg): 
        # Recieve messages. 
        self.message = msg 

    def header(self): 
        ''' Print the html header codes with title of application. ''' 
        output = ''' 
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://
        www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"
            dir="ltr">
            <head>
                <title>PyMyAdmin 0.001</title>
                <meta http-equiv="Content-Type" content="text/html;
                        charset=utf-8" />
            </head>
        <body>
        ''' 
        return output 

    def footer(self): 
        ''' Print html codes ''' 
        output = ''' </body>
                    </html> 
                    ''' 
        return output 

    def body(self): 
        output = '' 
        title = "<h1>PyMyAdmin </h1>" 
        output = output + title + "<br>" + self.message 
        return output 

    def page(self): 
        ''' Create webpage from output ''' 
        header = self.header() 
        body = self.body() 
        footer = self.footer() 
        output = header + body + footer 
        return output 


''' Function definition ''' 
def connectNoDB( user, password ): 
    ''' Create a databases connection and returns thr cursor ''' 
    try: 
        host = 'localhost' 
        mydb = mysql.connect(host=host,user=user,passwd=password) 
        cur = mydb.cursor() 
        return cur 
    except mysql.Error: 
        print("There was a problem in connecting to the database.")  
    except mysql.Warning: 
        pass 

def connection( user, password, database): 
    try: 
        host = 'localhost' 
        mydb = mysql.connect(host,user,password,database) 
        cur = mysql.cursor() 
        return cur 
    except mysql.Eorror: 
        print("There was a problem in connecting to the database.")  
    except mysql.Warning: 
        pass 

def dbaction( act, name, cursor ): 
    if act == 'create': 
        statement = 'CREATE DATABASE IF NOT EXISTS %s'%(name) 
        output = execute( statement, cursor, 'create-db' ) 
    elif act == 'drop': 
        statement = 'DROP DATABASE IF EXISTS %s'%(name) 
        output = execute( statement, cursor, 'drop-db' ) 
    else: 
        output = 'Bad information' 
    return output 

def tbaction( act, db, name, columns, types, user, password ): 
    cursor = connection( user, password, db ) 

    if act == 'create': 
        tname =  name +'(' 
        columns = columns.spilt(',') 
        types = types.spilt(',') 
        
        # Make <table name>( <column name> <data type> ) for creating table. 
        for i in range(len(columns)): 
            col = columns[i].strip() 
            val = types[i].strip() 
            tname = tname + col +' '+ val 
            # if it reaches at the end of the list, then add ')' 
            if i == len(columns)-1:  
                tname += ')' 
            else: 
                tname += ',' 
        statement = 'CREATE TABLE IF NOTE EXIST %s'%(tname) 
        results = execute( statement, cursor, 'create-tb' ) 

    elif act == 'drop': 
        statement = 'DROP TABLE IF EXISTS %s'%(name) 
        results = execute( statement, cursor, 'drop=tb' ) 
    return results 

def qaction( qact, db, tb, columns, values, user, password ): 
    cursor = connection( user, password, db ) 

    tname = tb + '(' 
    columns = columns.spilt(',') 
    values = values.spilt(',') 
    cols = '' 
    vals = '' 

    for i in range(len(columns)):
        col = columns[i].strip()
        val = valuse[i].strip() 
        cols += col 
        vals = vals+"'"+val+"'" 
        # if it doesn't reache at the end of the list, then add ',' 
        if i != len(columns)-1: 
            cols += ',' 
            vals += ',' 

    if qact == 'select': 
        statement = "SELECT * FROM %s WHERE %s = %s"%(tb,cols,vals) 
        results = execute( statement, cursor, 'select' ) 
    elif qact == 'insert': 
        statement = "INSERT INTO %s(%s) VALUES(%s)"%(tb,cols,vals) 
        results = execute( statement, cursor, 'insert' ) 

    return results 

def execute( statement, cursor, types ): 
    while True: 
        try: 
            cursor.execute(statement) 
            if types == 'select': 
                # Run query 
                output = cursor.fetchall() 
                results = '' 
                data = '' 
                for record in output: 
                    for entry in record: 
                        data = data + '\t' + str(entry) 
                    data += '\n' 
                results = results + data + '\n' 
            elif types == 'insert': 
                results = "Your information was inserted with following SQL statement: %s"%(statement) 
            elif types == 'creat-db': 
                results = "The following statement has been processed: %s"%(statement) 
            elif types == 'creat-tb': 
                results = "The following statement has been processed: %s"%(statement) 
            elif types == 'drop-db': 
                results = "The following statement has been processed: %s"%(statement) 
            elif types == 'drop-tb': 
                results = "The following statement has been processed: %s"%(statement) 

            return results 
        except mysql.Error as e: 
            print("Error raised, invalid input!") 
            print("Error msg: %s"%(e)) 
            raise e 
        except mysql.Warning: 
            pass 

def main(): 
    ''' 
    opt = optparse.OptionParser()
    opt.add_option("-U", "--user",
                    action="store",
                    type="string",
                    help="user account to use for login",
                    dest="user")
    opt.add_option("-P", "--password",
                    action="store",
                    type="string",
                    help="password to use for login",
                    dest="password")
    opt.add_option("-d", "--dbact",
                    action="store",
                    type="string",
                    help="kind of db action to be affected",
                    dest="dbact")
    opt.add_option("-D", "--dbname",
                    action="store",
                    type="string",
                    help="name of db to be affected",
                    dest="dbname")
    opt.add_option("-t", "--tbact",
                    action="store",
                    type="string",
                    help="kind of table action to be affected",
                    dest="tbact")
    opt.add_option("-Q", "--tbdbact",
                    action="store",
                    type="string",
                    help="name of database containing table to be affected",
                    dest="tbdbname")
    opt.add_option("-N", "--tbname",
                    action="store",
                    type="string",
                    help="name of table to be affected",
                    dest="tbname")
    opt.add_option("-q", "--qact",
                    action="store",
                    type="string",
                    help="kind of query to affect",
                    dest="qact")
    opt.add_option("-Z", "--qdbname",
                    action="store",
                    type="string",
                    help="database to be used for query",
                    dest="qdbname")
    opt.add_option("-Y", "--qtbname",
                    action="store",
                    type="string",
                    help="table to be used for query",
                    dest="qtbname")
    opt.add_option("-c", "--columns",
                    action="store",
                    type="string",
                    help="columns to be used in query",
                    dest="columns")
    opt.add_option("-v", "--values",
                    action="store",
                    type="string",
                    help="values to be used in query",
                    dest="values")
    opt, args = opt.parse_args()
    ''' 

    form = cgi.FieldStorage() 

    user = form.getvalue('user') 
    password = form.getvalue('password') 

    dbact = form.getvalue('dbact') 
    dbname = form.getvalue('dbname') 

    tbact = form.getvalue('tbact') 
    tbdbname = form.getvalue('tbdbname') 
    tbname = form.getvalue('tbname') 

    qact = form.getvalue('qact') 
    qdbname = form.getvalue('qdbname') 
    qtbname = form.getvalue('qtbname') 
    columns = form.getvalue('columns') 
    values = form.getvalue('values') 

    output = '' 
    while 1: 
        try: 
            cursor = connectNoDB( user, password ) 
            authentic = 1 
        except: 
            output = 'Bad log information.' 
            authentic = 0 

        if authentic == 1: 
            errmsg = "You have not specified the information necessary for the action you chose." 

            if opt.dbact is not None: 
                output = dbaction( dbact, dbname, cursor ) 
            elif opt.tbact is not None: 
                output = tbaction( tbact, tbdbname, tbname, columns, values, user, password ) 
            elif opt.qact is not None: 
                output = qaction( qact, qdbname, qtbname, columns, values, user, password ) 
            else: 
                output = errmsg 
        
        printout = HTMLPage() 
        printout.message(output) 
        output = printout.page() 

        print(output) 
        break 




if __name__ == '__main__': 
    main() 



''' If use CGI: 

form = cgi.FieldStorage() 

user = form.getvalue('user') 
password = form.getvalue('password') 

dbact = form.getvalue('dbact') 
dbname = form.getvalue('dbname') 

tbact = form.getvalue('tbact') 
tbdbname = form.getvalue('tbdbname') 
tbname = form.getvalue('tbname') 

qact = form.getvalue('qact') 
qdbname = form.getvalue('qdbname') 
qtbname = form.getvalue('qtbname') 
columns = form.getvalue('columns') 
values = form.getvalue('values') 

''' 


