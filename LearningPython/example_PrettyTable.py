#!/usr/bin/python3.5 

from prettytable import PrettyTable 

# Define the names of column 
table_def = PrettyTable( [ 'Name', 'id', 'School' ] ) 

# Format 
table_def.align['Name'] = 'r' # let the column Name align along right.  
table_def.align['School'] = 'r' 

# Add values row by row 
table_def.add_row( [ 'Eason', 402352506, 'FJU' ] ) 
table_def.add_row( [ 'Johnny', 106258009, 'NCCU' ] ) 
table_def.add_row( [ 'Leticia', 403351614, 'FJU' ] ) 

# Print out the table 
print(table_def) 


