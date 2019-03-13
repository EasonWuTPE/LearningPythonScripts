#!/usr/bin/python3,5 

import MySQLdb as mysql 

# CONCAT() 
''' 
    CONCAT():
        This function provides us to concatenate, or join, two or more values. 

            $ SELECT CONCAT(value1, value2); 
''' 

# SUBSTRING(), MID() 
''' 
    SUBSTRING(), MID():　
        SUBSTRING() and MID() are the same. They allow us to extract a substring, or midsection, of a value within the bounds of certain index position. 

            $ SELECT SUBSTRING( value, position, length ); 
            $ SELECT MID( value, position, length ); 
        
        [Note]
        The value that is a type of string and position where starts at 1 not 0 are required and length is optional. 
        If length is ommited, MySQL will return it from position to the last. 
        Position of SUBSTRING() and MID() also provide counting backward from the end of the value by using negative number. 
        e.g. SELECT [SUBSTRING|MID]( value, -position ); 

''' 

# TRIM() 
''' 
    TRIM(): 
        The same function in the Python built-in function .strip() that get rid of the blank space of the string at front and back. 
        However, TRIM() is more flexible than .strip(), which can be customized to strip a specified values from the beginning of 
        value, the end of value, or both. 

            $ SELECT TRIM(<some value>); 
        
        [NOTE] <some value> can be numeric or string. 

    TRIM() with optional: 
        Using LEADING, TRAILING, BOTH to customized the TRIM() function. 

            $ SELECT TRIM( [LEADING|TRAILING|BOTH] <val 1> FROM <val 2> ); 

            e.g. $ SELECT TRIM( LEADING ' ' FROM '  ACB   ' ); 
                    -> stripping the leading blank from '  ABC  ' to 'ABC   '
            e.g. $ SELECT TRIM( TRAILING ' ' FROM '  ACB   ' ); 
                    -> stripping the last blank from '  ABC  ' to '   ABC'
            e.g. $ SELECT TRIM( BOTH ' ' FROM '  ACB   ' ); 
                    -> stripping the leading and last blank from '  ABC  ' to 'ABC'

    Alternatives: 
        LTRIM() strips blank space from left and RTRIM() strips blank space from right. 

''' 
# REPLACE() 
''' 
    REPLACE(): 
        Replace the val1 by val2 in strings or "numeric". 

            $ SELECT REPALCE( <base value>, <value to be replaced>, <replacement value> );

''' 
# INSERT() 
''' 
    INSERRT():
        Inserting the value from specified position or overwrite it. 

            $ SELECT INSERT( <base value>, <position>, <length to be overwite>, <string to be inserted> ); 
            
        If the lenght = 0, then no value of base value will be overwritten. 
''' 

# REGEXP 
''' 
    See more on page 350. 
''' 
# LENGTH() 
''' 
    LENGTH(): 
        The same as len() in Python. 
''' 

# INSTR(), LOCATE() 
''' 
    INSTRA(), LOCATE(): 
        Both INSTRA() and LOCATE() are returned index location of given string or "numeric". 

        $ SELECT INSTR( <base string>, <value to be found> ); 
        $ SELECT LOCATE( <value to be found>, <base string> ); 

        The arguments of these two functions are opposite position to each other. 

        [NOTE]
        INSTR() returns the index location when it meet the first occurence of the string. 
        Instead, LOCATE() can specify the beginning point of the search by starting the index point after the base string. 

            $ SELECT LOCATE( <value to be found>, <base string>, <specified position> ); 
            e.g. $ SELECT LOCATE( "C", "ABC#$@CDE", 4 ); 
                            --> 7 
''' 
# Nuancing data 

# ROUND()
''' 
    ROUND(): 
        The round down function. 
            
            $ SELECT ROUND( <base value>, <numbers of position> ); 

            [NOTE] 
            ROUND() is only used for numerical value. Otherwise, it returns zero values and warnings. 
''' 

# FORMAT() 
''' 
    FORMAT(): 
        Similar to ROUND() but making outputing more human-friendly by adding punctuation for the value. 

            $ SELECT ROUND( 10000/3, 5 ); 
                    --> 3333.33333 
            # SELECT FORMAT( 10000/3, 5 ); 
                    --> 3,333.33
''' 

# UPPER(), LOWER() 
''' 
    UPPER(), LOWER(): 
        Make strings to be upper or lower characters. 
        
            $ SELECT [UPPER|LOWER](<strings>); 
''' 


