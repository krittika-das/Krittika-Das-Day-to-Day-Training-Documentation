-- Create database
CREATE DATABASE retail_app;
USE retail_app;

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
-- Customers
INSERT INTO customers VALUES
(1,'Alice','alice@mail.com'),
(2,'Bob','bob@mail.com'),
(3,'Charlie','charlie@mail.com'),
(4,'Diana','diana@mail.com'),
(5,'Ethan','ethan@mail.com'),
(6,'Fiona','fiona@mail.com'),
(7,'George','george@mail.com'),
(8,'Hannah','hannah@mail.com'),
(9,'Ian','ian@mail.com'),
(10,'Jane','jane@mail.com');

-- Products
INSERT INTO products VALUES
(101,'Laptop','Electronics',800),
(102,'Phone','Electronics',600),
(103,'Shoes','Fashion',120),
(104,'Watch','Fashion',200),
(105,'Book','Stationery',30),
(106,'Pen','Stationery',5),
(107,'Headphones','Electronics',150),
(108,'Bag','Fashion',90),
(109,'Tablet','Electronics',400),
(110,'Notebook','Stationery',10);

-- Orders
INSERT INTO orders VALUES
(1001,1,101,1,'2025-01-10'),
(1002,1,103,2,'2025-02-15'),
(1003,2,102,1,'2025-03-20'),
(1004,2,105,3,'2025-03-22'),
(1005,3,107,1,'2025-04-05'),
(1006,3,108,2,'2025-04-07'),
(1007,3,109,1,'2025-05-01'),
(1008,4,104,1,'2025-05-10'),
(1009,5,106,5,'2025-06-12'),
(1010,5,101,1,'2025-06-15');

SELECT c.customer_id, c.name, COUNT(o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 2;

SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
WHERE o.product_id IS NULL;

SELECT c.customer_id, c.name,
       SUM(p.price * o.quantity) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name;

SELECT c.customer_id, c.name, o.order_id, o.product_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

SELECT p.product_id, p.product_name, o.order_id, o.customer_id
FROM orders o
RIGHT JOIN products p ON o.product_id = p.product_id;

SELECT c.customer_id, c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING COUNT(DISTINCT p.category) > 1;

SELECT o.order_id, c.name,
       (p.price * o.quantity) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
ORDER BY revenue DESC
LIMIT 3;

SELECT *
FROM orders
WHERE customer_id IS NULL OR product_id IS NULL;

SELECT c.customer_id, c.name,
       MONTH(o.order_date) AS month,
       SUM(p.price * o.quantity) AS total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name, MONTH(o.order_date)
ORDER BY c.customer_id, month;

SELECT c.customer_id, c.name, p.product_id, p.product_name
FROM customers c
CROSS JOIN products p;
