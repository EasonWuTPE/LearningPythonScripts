create database if not exists mydb; 
use mydb; 
create table if not exists mytable( 
	id	int unsigned not null auto_increment, 
    username varchar(50) not null, 
    email varchar(40) not null, 
    primary key (id) 
); 

# Insert data 
insert into mytable (username,email) values ("ABC","ABC@examples.com"); 
insert into mytable (username,email) values ("abc","abc@examples.com"); 
insert into mytable (username,email) values ("aBc","aBc@examples.com"); 
insert into mytable (username,email) values ("AbC","AbC@examples.com"); 

# Update the a row into data 
update mytable set username="abc" where id=8; 

# Delete data 
delete from mytable where id=7; 

# select all data from table 
select * from mytable; 
select distinct id from mytable; # select column id from table 
select * from mytable where username='ABC'; # select all whose username is ABC from table 
