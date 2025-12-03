import pymysql

conn=pymysql.connect(host='localhost',user='root',password='Memories000%',db='retail_db')
cursor=conn.cursor()

cursor.execute("select * from Customers")

rows=cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()