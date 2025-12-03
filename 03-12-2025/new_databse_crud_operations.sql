CREATE DATABASE college_db;
USE college_db;
CREATE TABLE student(student_id INT auto_increment PRIMARY KEY, first_name VARCHAR(50), last_name varchar(50), email varchar(100), age int, city varchar(50));
INSERT INTO student(first_name, last_name, email, age, city) values ('Aisha', 'Zulkar', 'aishazulkar@gmail.com', 45, 'Kolkata')
INSERT INTO student(first_name, last_name, email, age, city) values ('Rohan', 'Mehra', 'rohanmehra@gmail.com', 22, 'Delhi')
select * from student
INSERT INTO student(first_name, last_name, email, age, city) values ('Madan', 'Mohan', 'madanmohan@gmail.com', 65, 'Hyderabad')
select first_name, last_name from student
select * from student order by age desc
update student set city='Bangalore' where student_id=2;
select * from student
delete from student where student_id=2
select * from student
drop table student;
drop database college_db;