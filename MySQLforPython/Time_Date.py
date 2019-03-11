#!/usr/bin/python3.5 

import MySQLdb as mysql 

''' 
    Five data types: DATETIME, DATE, TIMESTEMP, TIME, YEAR 
    These data types of time are used when construct a table like INT, VARCHAR. The input format of date/time data type is a string.  
''' 

# DATETIME 
''' 
    1. DATETIME: 
        It is used to specify a value thate includes both date and time. It doesn't generate values automatically but be inputed by users. 
        
        1.1 Output format: 
            DATETIME recieve several formats but return only one format: YYYY-MM-DD HH:MM:SS 

        1.2 Input formats: 
            I. Four- or Two- digit year. 
                e.g. YYYY-MM-DD HH:MM:SS or YY-MM-DD HH:MM:SS 
            II. Any delimiter as long as consistently applied. 
                e.g. YYYY.MM.DD HH@MM@SS or YY/MM/DD HH*MM*SS 
            III. No delimiter. 
                e.g. YYYYMMDDHHMMSS 
            IV. No delimiter with two-digit year. 
                e.g. YYMMDDHHMMSS 
        
        1.3 Input range: 
            It must start after millennium CE-1000-01-01 and before 9999-12-31 23:59:59. Any values out of this range will result in 0000-00-00 00:00:00. 

''' 

# DATE 
''' 
    2. DATE: 
        As its name, it's a day. 

        2.1 Output format: 
            As DATETIME but only first half of DATETIME: YYYY-MM-DD 

        2.2 Input Formats:
            As DATETIME but only first halt of DATETIME. 
            I. Four- or Two- digit year. 
                e.g. YYYY-MM-DD or YY-MM-DD 
            II. Any delimiter as long as consistently applied. 
                e.g. YYYY.MM.DD or YY/MM/DD  
            III. No delimiter. 
                e.g. YYYYMMDD 
            IV. No delimiter with two-digit year. 
                e.g. YYMMDD 

        2.3 Input range: 
            As DATETIME but only first half of DATETIME  
            
''' 

# TIMESTAMP 
''' 
    3. TIMESTAMP: 
        It is a auto-generated data type. Therefore, its value is not specified in INSERT statement but is culled from the server's local time. 
        It follows the same format in DATETIME: YYYY-MM-DD HH:MM:SS. This is fixed width and cannot be changed. 
    
        3.1 Inputs: 
            It is a auto-generated data type. Therefore, its value is not specified in INSERT statement but is culled from the server's local time. 
            MySQL always deals in UTC internally. If the server is not on UTC, the server's time is converted to UTC in order of data storage and then convert back when data is requested. When using INSERT and SELECT at different time zone, MySQL will auto-convert the TIMESTAMP. 

        3.2 Input range: 
            The input range of TIMESTAMP is more restricted than DATETIME. 
            Because of using system time, it uses Unix time as its beginning of its range: 1970-01-01 00:00:01, which lead to 0 when it is invalid.  
            *** Note: So, 1963-11-22 12:02:01 can be used as a DATETIME but TIMESTAMP. 

        3.3 Default, initializing, and updating of TIMESTAMP. 
            >> $ TIMESTAMP DEFAULT <value>  # Initialize the TIMESTAMP 
            >> $ TIMESTAMP DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP # Initialize the TIMESTAMP of 0 but requests updating to the current timestamp
            >> $ TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP # Set the TIMESTAMP to system time at initialization and then update it. 

''' 
        
# YEAR 
''' 
    4. YEAR: 
        As the name implies, the YEAR only stores year. 

        4.1 Output: 
            Whether the year is two- or four-digit depends on what you type. 
            YYYY or YY 

        4.2 Inputs: 
            I. Two-digit: 
                YEAR(2), from 1970 to 2069. (99 years) 
            II. Four-digit: 
                YEAR(4), from 1901 to 2155. 

        4.3 Invalid inputs: 
            YEAR(2) accepts two-digit inputs, but YEAR(4) can accept 2- or 4-digit inputs. 
            YEAR(4) with two-digit inputs will be recognized to belong 21th century, except for 70, 90 and 00. 
            70, 90 and 00 will render as 1970, 1999 and 2000. 

''' 

# TIME 
''' 
    5. TIME: 
        It is used for 3 purpose. 
        I. A time of day. 
        II. An elapse time. 
        III. An interval of time. 

        5.1 Format: 
            Output data is only in one format: HH:MM:SS 
            INputs: 
                I. "HHMMSS" or HHMMSS, a string data type or integer. 
                II. Colons for delimiter: HH:MM:SS 
                III. days + time: D HH:MM:SS 
        5.2 Invalid inputs: 
            Invalid TIME values are zeroed out to 00:00:00. More on pp.255 

''' 
# Date and Time function on pp.257 
''' 
    DATE(), YEAR(), DATE_ADD(), DATEDIFF()...... 
''' 


