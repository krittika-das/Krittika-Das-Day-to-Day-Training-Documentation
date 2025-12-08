create database company;
use company;

create table employees(
id int auto_increment primary key,
name varchar(50),
role varchar(50),
salary int);

CREATE TABLE departments (
dep_id int auto_increment primary key,
id int,
name VARCHAR(100) NOT NULL,
location VARCHAR(100)
);

insert into employees (name, role, salary) values("Krittika", "IT", 50000), ("Rohan", "HR", 8000)
insert into departments (id, name, location) values(1, "Dept-IT", "Kolkata"), (2, "Dept-HR", "Hyderabad")