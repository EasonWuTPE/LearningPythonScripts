#!/usr/bin/python3.5 

''' 
    Notes for module csv 
''' 

import csv 

# Read 
with open('iris.csv', newline='') as csvfile: 
    ''' 
        newline make sure that the any characters including '\n' can be parsed correctly. 
    ''' 
    rows = csv.reader(csvfile,delimiter=',') # csv.reader returns a 2-d list. [ [line 1], [line 2], [line 3], ... ] 
    print("\n\n****csv.reader(<file object>)****") 
    for row in rows: 
        print(row) 

with open('iris.csv', newline='') as csvfile: 
    ''' 
        csv.DictReader( <file object> ) returns a dictionary. It uses the first row to the key of dict as column names. 
    ''' 
    rows = csv.DictReader(csvfile, delimiter=',')
    print("\n\n****csv.DictReader(<file object>)****") 
    for row in rows: 
        print( row['sepal_length'], row['petal_width'] ) 

# Output 
with open('output_csv_module1.csv', 'w', newline='') as csvfile: 
    ''' 
        csv.writer( <file object> ) 
    ''' 
    writer = csv.writer(csvfile, delimiter=',') # delimiter = ',' is default. 

    writer.writerow(['name','height','weight']) # .writerow() write to csv row by row 

    writer.writerow(['Eason',177,68]) 
    writer.writerow(['Leticia',169,52]) 




record = [ ['name','height','weight'],
           ['Eason',177,68],
           ['Leticia',168,52] ] 
with open('output_csv_module2.csv', 'w', newline='') as csvfile: 
    ''' 
        csv.writer( <file object> ) 
    ''' 
    writer = csv.writer(csvfile, delimiter=',') # delimiter = ',' is default. 

    writer.writerows( record ) # .writerows() write the list to csv 



with open('output_csv_module3.csv', 'w', newline='') as csvfile: 
    ''' 
        csv.DictWriter( <file object>, fieldnames ) 
    ''' 
    col_name = ['name','height','weight'] 
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames = col_name) # fieldnames is the list of column names. 

    writer.writeheader() # Write the column names for the first row. 

    writer.writerow({'name':'Eason','height':177,'weight':68}) 
    writer.writerow({'name':'Leticia','height':169,'weight':52}) 




