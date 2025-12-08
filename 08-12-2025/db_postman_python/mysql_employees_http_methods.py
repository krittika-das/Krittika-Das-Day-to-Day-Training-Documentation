from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123Wed*%^",
        database="company",
        cursorclass=pymysql.cursors.DictCursor  # rows as dicts
    )

@app.get('/employees')
def get_employee():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.post('/employees')
def add_employee():
    data = request.json
    name = data['name']
    salary = data['salary']
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", (name, salary))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Employee added"}), 201

@app.put('/employees/<int:id>')
def update_employee(id):
    data = request.json
    name = data.get('name')
    salary = data.get('salary')
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name=%s, salary=%s WHERE id=%s", (name, salary, id))
    conn.commit()
    updated = cursor.rowcount
    cursor.close()
    conn.close()
    if updated == 0:
        return jsonify({"message": "Employee not found"}), 404
    return jsonify({"message": "Employee updated"})

@app.delete('/employees/<int:id>')
def delete_employee(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    conn.commit()
    deleted = cursor.rowcount
    cursor.close()
    conn.close()
    if deleted == 0:
        return jsonify({"message": "Employee not found"}), 404
    return jsonify({"message": "Employee deleted"})

if __name__ == '__main__':
    app.run(debug=True)