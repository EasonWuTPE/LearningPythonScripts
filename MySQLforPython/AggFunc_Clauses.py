#!/usr/bin/python3.5 

import MySQLdb as mysql 

''' 
    Aggregated functions: 

    COUNT(): Returns only non-null results. 
    SUM(): Returns total series of numeric values.  
    MAX(): 
    MIN(): 
    AVG(): Mean of series of numeric values, 

    Each of these functions is called by inserting the functiom's name and arguement immediately after SELECT. 
    e.g. 
        $ SELECT AggFunc(<column name>) FROM <table name>; 

    [Note]: 
    1. Only COUN(), MAX(), MIN() can handle string data. 
    2. Mode, Median are calculated on your own. 
        *Mode in odd number of items: SELECT <col> from <table> ORDER BY <col> DESC LIMIT <half the total number of items>, 1; 
        *Mode in even number of items: SELECT <col> from <table> ORDER BY <col> DESC LIMIT <half the total number of items>, 2;
            ->then calculate the mean of two numbers. 
''' 
''' 
    Trimming data: 

    Two ways to trimming data when using aggregation function. One is DISTINCT that remove redundant data. The other is GROUP_CONCAT() pools the data into single string data. 

    1. DISTINCT: 
        Remove redundant data to ensure that every values are unique. Aggregated functions cannot deal with the redundant data. 
        DISTINCT can be used with COUNT(), MAX(), MIN() and AVG(). Note that DISTINCT can be used without any aggregated functions.

        $ SELECT DISTINCT <col name> FROM <TABLE>; 
        $ SELECT AggFunc(DISTINCT <col name>) FROM <TABLE>; 
                where AggFunc is COUNT(), MAX(), MIN(), AVG(). 

    2. GROUP_CONCAT() 
        The GROUP_CONCAT() collates all of the results into a single string value. By default, they are separated by ',' and you can setting any delimiter by clause SEPARATOR option. One must note that GROUP_CONCAT() only returns 1024 characters. 

        $ SELECT GROUP_CONCAT( <col name> [SEPARATOR <"any char">]) FROM <table name>; 

    [Note] GROUP_CONCAT() doesn't sort the values. It can be used with DISTINCT. 
        $ SELECT GROUP_CONCAT( [DISTINCT] <col name> [SEPARATOR <"any char">]) FROM <table name>; 

''' 
''' 
    GROUP BY v.s. ORDER BY: 


''' 


