select * from subscriptions where expiry_date <= current_date + INTERVAL 10 day

select * from subscriptions where month(start_date) = Month(Current_date) and year(start_date) = year(current_date) 

select * from subscriptions where plan_type='Yearly' order by expiry_date asc

select * from subscriptions where datediff(expiry_date, start_date)>30

select * from subscriptions where expiry_date < start_date