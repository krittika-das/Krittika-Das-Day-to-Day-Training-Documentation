import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="s27&6g%",
    database="company_db"
)

cursor = conn.cursor()

def addemp(name, dept, salary):
    query = "INSERT INTO employess (name, dept, salary) VALUES (%s, %s, %s)"
    data=(name, dept, salary)
    cursor.execute(query, data)
    conn.commit()

def viewall():
    query = "SELECT * FROM employess"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

def update_salary(empid, new_salary):
    query = "UPDATE employess SET salary = %s WHERE empid = %s"
    cursor.execute(query, (new_salary, empid))
    conn.commit()

addemp('Krittika', 'Advanced Engineering', 35000)
addemp('Priyanka', 'SAP', 32900)
addemp('Madhusmita', 'Cloud', 12000)

viewall()

update_salary('1', 54000)

viewall()


