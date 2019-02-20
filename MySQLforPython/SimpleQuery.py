#!/usr/bin/python3.5 

import MySQLdb as mysql 

''' Four basic concepts ''' 
''' 
    CRUD: 
    1. Create 
    2. Read 
    3. Update 
    4. Delete 

''' 
'''
    MySQL: 
        
        SELECT {*|column_name} FROM {table_name};
        SELECT {*|column_name} FROM {table_name} [WHERE where_condition];
        SELECT {*|column_name} FROM {table_name} [GROUP BY {col_name|position|expr} [ASC|DESC], [WITH ROLLUP], [HAVEING where_condition]];
                                        where [with rollup] provides for a summative line at the end of the results, 
                                              and [HAVING] is used to  quantify results acording to aggregate functions, which is usually in conjuction with GROUP BY. 
        SELECT {*|column_name} FROM {table_name} [ORDER BY {col_name|position|expr} [ASC|DESC]]; 
                                        where ORDER BY can be used in conjuction with GROUP BY. 

                            [LIMIT arg1, arg2 ] where arg1 is the (arg1+1)th position and arg2 values from (arg1+1)th. 
                            [INTO OUTFILE 'location+filename'] output to a text file. This may encounter problems. 

            ** HAVING is applied as parameters of the search before MySQL actions the query, 
               LIMIT is applied after the search results have been return. 
'''






