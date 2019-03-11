#!/usr/bin/python3.5 


# HAVING v.s. WHERE: 
''' 
    HAVING v.s. WHERE: 
    Difference in: 

    1. Syntax: 
        The HAVING can only be applied to the columns that have been previously indicated in the SELECT statement.
        e.g. $ SELECT <columns(s)> FROM <table> HAVING <certain condition met in column(s) before>; 
        i.e. the condition in HAVING clause must appear in the selected columns. 

    2. Aggregate functions: 
        The use of aggregate functions. 
        HAVING clause with aggregate functions must be placed in the GROUP BY structure. HAVING clause is applied after aggregation is performed. 

        [Note] 
        As mentioned above, HAVING requires the column used in its condition to have been mentioned in SELECT statement previously. 
        But the columns passed as arguemnts to aggregate function to calculate do not be considered as being mentioned previously. 
        Actually, MySQL doesn't see them when evalute a HAVING clause, which means MySQL just sees the results of aggregate function. 
        Rather, if one wants to use the columns mentioned in aggregate function within SELECT statement, we need to give them a name using AS.
        
            $ SELECT <col1 name | AggFunc(col2 name)> FROM <table> HAVING <col2 name condition>;            --> This may lead to errors. 
            $ SELECT < col1 name | AggFunc(col2 name) AS <name2> > FROM <table> HAVING <name2 condition>; 

    3. Application: 
        Whenever you pass a SELECT statement to MySQL, it forms a table of results which is then optimized. 
        The condition in WHERE is applied before the optimizers are carried out. 
        The condition in HAVING is applied after the optimizers are carried out. 
        These differences are affected as a final filter for what should be reported back. 
        The difference is subtle, but boils down to application before the results are finalized and application after the result table is created. 

        See more on p.316. 


    [Conclusion] 
    1. HAVING condition must be indicated in the SELECT statement previuosly. 
    2. HAVING condition with aggregate functions must bt placed in the GROUP BY statement. 
       If one wants to use the argument of the aggregate function in SELECT, referenced the aggregate function AS another variable is required, because of the priority of the evaluation of the aggregate function. 
    3. MySQL executes the WHERE condition before optimizing and executes the HAVING statement after the optimizing. 
       i.e. WHERE reduce the amount of data through a simple filter, and HAVING filters the results. 

''' 

# Subquery 
''' 
    Subquery: 
        One wants to use the first result of query to be as input for another query with one statement. 
        
        $ SELECT <column reference> FROM <table1> WHERE <a column from table1>  <relational operator> (SELECT <a similar column from table2> FROM <table>); 
                where <relational operators are >, <, =, ANY, IN... so on. 


''' 

# UNION  
''' 
    Union 
        The union is the combination of the results from two SELECT statements into a single result set. 
        
            $ (<SELECT statements 1>) UNION (<SELECT statements 2>); 

        The numbers of the columns that is returned by each SELECT statements must be equal, or thrown an error. 
        The name of returned table depends on the selected column on the left of UNION. 
        The data type of each column should be the same with the respect to the columns of the other statement. Otherwise, it will throw strange results. 

''' 

# JOIN 
''' 
    JOIN: 

''' 


