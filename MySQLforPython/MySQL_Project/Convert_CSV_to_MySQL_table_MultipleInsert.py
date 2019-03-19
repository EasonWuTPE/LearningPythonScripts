#!/usr/bin/python3.5 

# Convert a CSV file to a MySQL table. 
# Multiple insertion. 


# Import Packages 
import MySQLdb as mysql 
import optparse 
import os 


opt = optparse.OptionParser() 
opt.add_option('-d','--database',action='store',type='string',help='name of local databases',dest='database') 
opt.add_option('-t','--table',action='store',type='string',help='table in indicated databases',dest='table') 
opt.add_option('-f','--file',action='store',type='string',help='file to be processed',dest='files') 
opt.add_option('-F','--Feilds',action='store',type='string',help='Feilds of the file to be processed', dest='Feilds') 
opt.add_option('-p','--passwd',action='store',type='string',help='Password to MySQL', dest='password') 
opt, args = opt.parse_args() 

# Store user inputs 
database = opt.database 
table = opt.table 
password = opt.password  
files = opt.files 
feilds = opt.Feilds.split(',') 
for i in range(len(feilds)): 
    feilds[i] = "'"+feilds[i].strip()+"'" 

def connection(database): 
    try: 
        mydb = mysql.connect( host='localhost', user='root', passwd=password, db=database ) 
        cur = mydb.cursor() 
        return cur 
    except mysql.Error as e: 
        print("Probelms occur when connecting to database.") 
        raise e
    except mysql.Warning: 
        pass 


def convert(files): 
    ''' Convert the file into MySQL table, which return a dictionary type.  ''' 
    import csv 
    filehandle = open(files) 
    sheet = csv.DictReader(filehandle,feilds) 
    return sheet 

def main(): 
    cursor = connection(database) 
    data = convert(files) 
    filesize = os.path.getsize(files) 
    
    values = []
    r = 0 
    for a in data: 
        if r == 0: # if r == 0, we are at the first record which is the column headers. 
            columns = ','.join(feilds) 
        else: # if r != 0, we have reocrd with actual data. 
            value ='' 
            for column_no in range(len(feilds)): 
                if column_no == 0: 
                    value = "'"+a[feilds[column_no]] 
                else: 
                    value += "','"+a[feilds[column_no]] 
            value += "'" 
        
        if r > 0: 
            if filesize <= 1000000:
                value = eval(value) 
                values.append(value) 
            else: 
                query = "INSERT INTO %s(%s) VALUES"%(table,columns) 
                statement = query +"("+values+")" 
                cursor.execute(statement) 
        r += 1 
    
    if filesize <= 1000000: 
        query = "INSERT INTO"+table+"("+columns+") VALUES(%s" 
        for i in range(len(feilds)-1): 
            query += +", %s" 
        query += ")" 
        query = str(query) 
        affected = cursor.executemany(query,values) 
        print("{} rows affected.".format(affected)) 
    else: 
        print("{} rows affected.".format(affected)) 


if __name__ == '__main__': 
    main() 



