/* Rbms 
in this rows,cloumns,feilds are present
column is verticle entity of specific table */


create table students (
    sid int primary key auto_increment,
    name varchar(50) Not null,
    email varchar(50) default null,
    roll int,
)


insert into students (sid,name,email,roll) values (
    (1,'abc','abc@gmail.com',10),
    (2,'pqr','pqr@gmail.com',11)
)

insert new values at sepcific id ->
UPDATE Customers SET Email = 'new.email@example.com', Phone = '555-123-4567' WHERE CustomerID = 123;


unqiue values of columns ->
select distinct column_name from table;

first 3 characters of column entries->
select substring(column_name,1,3) from students;

unique values of major ubject nd print length
select distinct major,length(major) from student;

select queries form major subject and replace a with A ->
select replace(first_name,'a','A') from student

combine 2 columns and print result in ans column
select concat(first,last) as name from student;

nested queries
alter table students alter column email varchar(100)

