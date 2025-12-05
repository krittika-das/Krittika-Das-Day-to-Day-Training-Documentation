CREATE DATABASE subscription_app;
USE subscription_app;
CREATE TABLE subscriptions (
sub_id INT PRIMARY KEY,
customer_name VARCHAR(50),
start_date DATE,
expiry_date DATE,
created_at DATETIME,
plan_type VARCHAR(20) -- Monthly, Quarterly, Yearly
);

INSERT INTO subscriptions VALUES
(1, 'Aisha Khan', '2024-12-15', '2025-01-15', '2024-12-15 10:30:00', 'Monthly'),
(2, 'Rahul Sharma', '2025-01-05', '2025-02-05', '2025-01-05 09:45:00', 'Monthly'),
(3, 'Imran Ali', '2025-02-10', '2025-03-10', '2025-02-10 14:12:00', 'Monthly'),
(4, 'Meera Iyer', '2025-03-01', '2025-04-01', '2025-03-01 17:05:00', 'Monthly'),
(5, 'Sanjay Patel', '2025-02-20', '2025-03-20', '2025-02-20 13:00:00', 'Quarterly')