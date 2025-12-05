CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    order_date DATE
);

INSERT INTO orders (customer_name, product_id, quantity, price, order_date) VALUES
('Alice', 101, 2, 500.00, '2025-12-01'),
('Bob', 102, 1, 1200.00, '2025-12-02'),
('Charlie', 103, 3, 150.00, '2025-12-02'),
('David', 101, 1, 500.00, '2025-12-03'),
('Eva', 104, 5, 80.00, '2025-12-03'),
('Frank', 105, 2, 300.00, '2025-12-04'),
('Grace', 102, 2, 1200.00, '2025-12-04'),
('Hannah', 103, 4, 150.00, '2025-12-05'),
('Ian', 104, 3, 80.00, '2025-12-05'),
('Jack', 105, 1, 300.00, '2025-12-05');


