create database company;
use company;
create table employees( id int auto_increment primary key, name varchar(50), salary int);
insert into employees(name, salary) values('John', 400000), ('Anna', 500000);
