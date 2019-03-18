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
    2. HAVING condition with aggregate functions must be placed in the GROUP BY statement. 
       If one wants to use the argument of the aggregate function in SELECT, referenced the aggregate function AS another variable is required, because of the priority of the evaluation of the aggregate function. 
    3. MySQL executes the WHERE condition before optimizing and executes the HAVING statement after the optimizing. 
       i.e. WHERE reduce the amount of data through a simple filter, and HAVING filters the results. 

''' 

# Subquery 
''' 
    Subquery: 
        One wants to use the first result of query to be as input for another query with one statement. 
        
        $ SELECT <column reference> FROM <table1> WHERE <a column from table1>  <relational operator> (SELECT <a "similar" column from table2> FROM <table>); 
                where <relational operators are =, = ANY, IN... so on. 

        e.g. $ SELECT title FROM film WHERE film_id = ( SELECT film_id FROM film_actor WHERE film_id='17' AND film_id='3'); 

        [Note] 
            In order to have MySQL process for each row of a series in sequence, use IN or ANY. 
                IN: be used to process an expression list. 
                = ANY: be used on the right side of any relational operator to cause MySQL to process any True value that is returned. 

''' 

# UNION  
''' 
    Union 
        The union is the combination of the results from two SELECT statements into a single result set. 
        
            $ (<SELECT statements 1>) UNION (<SELECT statements 2>); 

        The numbers of the columns returned by each SELECT statements must be equal, or thrown an error. 
        The name of returned table depends on the selected column on the left of UNION. 
        The data type of each column should be the same with the respect to the columns of the other statement. Otherwise, it will throw strange results. 
        [Note] The columns in one table must appear in the other table and the data type of both SELECT are the same. Otherwise, it runs strange. 

''' 

# The JOIN and UNION in MySQL are not the same concept of Math. 

# LEFT|RIGHT|FULL JOIN 
''' 
    JOIN: 
        Each set is represented by a table. The first table referenced in the query is the set on the left, the second is presented by another.
        LEFT or RIGHT JOIN are types of OUTER JOIN, which is specified by user or LEFT by default. 

            $ SELECT <cols to be returned> FROM <table1> <LEFT|RIGHT> JOIN <table2> ON <key col from table1> <relational operator> <key col from table2>;
        
        Whichever table is specified as primary is returned in full by default. 
        If there exists different length of two tables, 
            a LEFT JOIN will result in the left set being exhaused, a RIGHT will use right set primary. 
        If the primary set is shorter, the non-primary set will be truncated to fit. 
        If the non-primary set is shorter, NULL will be return to complement to primary sets values. 

            e.g. $ SELECT birth as Birth FROM Birthdaytab2 LEFT|RIGHT JOIN studentstable ON birthdaytab2.id = studentstable.id; 

        [Note] FULL JOIN in MySQL equals to the concept of union in Math. 
''' 

# OUTER JOIN 
''' 
    OUTER JOIN: 
        The LEFT|RIGHT|FULL JOIN are types of OUTER JOIN. 
        This means that LEFT|RIGHT|FULL JOIN equals to LEFT|RIGHT|FULL OUTER JOIN, which OUTER is optional and can be ommited. 

''' 

# INNER JOIN 
''' 
    INNER JOIN: 
        The intersection of sets. The concept of INNER JOIN in MySQL is the same as the intersection in Math. 

            $ SELECT <cols to be returned> FROM <table1> INNER JOIN <table2> ON <key col from table1> <relational operator> <key col from table2>;
''' 

# NATURAL JOIN 
''' 
    NATURAL JOIN: 
        Very close concept of INNER JOIN above. 

            $ SELECT <cols in tab1> FROM <tab1> NATURAL JOIN <tab2>; 
''' 

# NATURAL LEFT|RIGHT JOIN 
''' 
    NATURAL LEFT|RIGHT JOIN: 

            NATURAL LEFT JOIN equals to LEFT [OUTER] JOIN  
            NATURAL RIGHT JOIN equals to RIGHT [OUTER] JOIN  

            $ SELECT <cols in tab1> FROM <tab1> NATURAL <LEFT|RIGHT> JOIN <tab2>; 
''' 

# CROSS JOIN 
''' 
    CROSS JOIN: 
        CROSS JOIN return every record of table 2 of table 1 without condition clause. 
            
            $ SELECT <cols in table 1>, <cols in table 2> FROM <table 1> CROSS JOIN <table 2>; 

''' 




