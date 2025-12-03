import pymysql

conn=pymysql.connect(host='localhost',user='root',password='Memories000%',db='retail_db')
cursor=conn.cursor()

cursor.execute("select * from Customers")

rows=cursor.fetchall()

for row in rows:
    print(row)

sql="Insert into Customers(customer_id,  customer_name,email, city) values(%s, %s, %s, %s)"
values=(110, "Rahul", "rahul@gmail.com", "Delhi")
cursor.execute(sql,values)
conn.commit()
print(cursor.rowcount)

cursor.execute("select * from Customers")

rows=cursor.fetchall()

for row in rows:
    print(row)

sql="Delete from Customers where name=%s"
values=("Rahul",)
cursor.execute(sql,values)
conn.commit()
print(cursor.rowcount, "record deleted")
cursor.execute("select * from Customers")
rows=cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()