CREATE DATABASE retail_db; 
USE retail_db; 

 CREATE TABLE customers ( 
    customer_id INT PRIMARY KEY, 
    customer_name VARCHAR(50), 
    email VARCHAR(80), 
    city VARCHAR(50)
 ); 
 
  CREATE TABLE orders ( 
    order_id INT PRIMARY KEY, 
    order_date DATE, 
    customer_id INT NULL, 
    total_amount DECIMAL(10,2), 
    product_id INT NULL 
);

 CREATE TABLE products ( 
    product_id INT PRIMARY KEY, 
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2) 
);

 INSERT INTO customers VALUES 
(1, 'Aisha Khan', 'aisha@xyz.com', 'Mumbai'), 
(2, 'Rahul Sharma', 'rahul@xyz.com', 'Delhi'), 
(3, 'John Daniel', 'john@xyz.com', 'Bangalore'), 
(4, 'Meera Iyer', 'meera@xyz.com', 'Chennai'), 
(5, 'Sanjay Patel', 'sanjay@xyz.com', 'Hyderabad'); 

 INSERT INTO products VALUES 
(101, 'Laptop HP 15', 'Electronics', 52000), 
(102, 'Samsung Phone A54', 'Electronics', 28000), 
(103, 'Jeans Blue Fit', 'Fashion', 1500), 
(104, 'T-Shirt Classic', 'Fashion', 700), 
(105, 'Wireless Mouse', 'Accessories', 900), 
(106, 'Rice 5KG Bag', 'Groceries', 320), 
(107, 'Olive Oil 1L', 'Groceries', 540), 
(108, 'Printer Canon G2012', 'Electronics', 12500);

 INSERT INTO orders VALUES 
(1001, '2024-01-05', 1, 52000, 101), 
(1002, '2024-01-06', 2, 28000, 102), 
(1003, '2024-01-07', 3, 1500, 103), 
(1004, '2024-01-07', 1, 700, 104), 
(1005, '2024-01-08', 2, 900, 105), 
(1006, '2024-01-08', NULL, 320, 106),    
(1007, '2024-01-09', 1, 540, NULL),     -- customer unknown -- product unknown 
(1008, '2024-01-10', 3, 12500, 108), 
(1009, '2024-01-10', 4, 320, 106), 
(1010, '2024-01-11', NULL, 700, 104),   -- customer null 
(1011, '2024-01-12', 2, 540, 107);      -- product exists but never order

select c.customer_name, c.email, p.product_name from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id

select p.product_name, p.category, p.price from Products p inner join Orders o on p.product_id=o.product_id

select c.customer_name, p.product_name from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id

select c.customer_name, o.total_amount from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id

select c.customer_name, p.product_name from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id where p.category='Electronics'

select c.customer_name from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id where category='Fashion'

select distinct c.customer_name from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id where c.city='Mumbai'

select c.customer_name, count(p.product_id) from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id group by c.customer_name

select c.customer_name, sum(o.total_amount) from Customers c inner join Orders o on c.customer_id=o.customer_id inner join Products p on o.product_id=p.product_id group by c.customer_name

select o.order_id, order_date, c.customer_id from Orders o left join Customers c on c.customer_id=o.customer_id

select o.order_id, c.city from Orders o left join Customers c on c.customer_id=o.customer_id

select c.customer_name, count(o.order_id) from Customers c left join Orders o  on c.customer_id=o.customer_id group by c.customer_name

select o.order_id, COALESCE(c.customer_name, 'Guest Checkout') from Orders o left join Customers c on c.customer_id=o.customer_id

select o.order_id, c.customer_name from Orders o left join Customers c on c.customer_id=o.customer_id where o.product_id=NULL

select o.order_id, c.customer_name from Orders o left join Customers c on c.customer_id=o.customer_id where c.city='Delhi'

select count(*) as Total_count from Orders o left join Customers c on c.customer_id=o.customer_id

select (count(c.customer_id is null)*100/  count(*)) from Orders o left join Customers c on c.customer_id=o.customer_id
