from flask import Flask, request, jsonify
import mysql.connector
import logging

app = Flask(__name__)


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

def get_db():
    logging.debug("Attempting DB connection...")
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Memories000%",
            database="company"
        )
        logging.debug("DB connection successful.")
        return db
    except Exception as e:
        logging.error(f"DB connection failed: {e}")
        raise

@app.route("/employees", methods=["GET"])
def get_employees():
    logging.debug("GET /employees called")
    try:
        db = get_db()
        cursor = db.cursor()
        logging.debug("Executing SELECT query")
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        logging.debug(f"Rows fetched: {rows}")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in GET: {e}")
        return "GET ERROR", 500


@app.route("/employees", methods=["POST"])
def add_employee():
    logging.debug("POST /employees called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)"
        logging.debug(f"Executing INSERT: {sql}")

        cursor.execute(sql, (data["name"], data["role"], data["salary"]))
        db.commit()
        db.close()

        logging.debug("POST completed")
        return "POST EXECUTED"
    except Exception as e:
        logging.error(f"Error in POST: {e}")
        return "POST ERROR", 500


@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    logging.debug(f"PUT /employees/{id} called")
    try:
        data = request.get_json()
        logging.debug(f"Received JSON: {data}")

        db = get_db()
        cursor = db.cursor()

        sql = "UPDATE employees SET name=%s, role=%s, salary=%s WHERE id=%s"
        logging.debug(f"Executing UPDATE: {sql}")

        cursor.execute(sql, (data["name"], data["role"], data["salary"], id))
        db.commit()
        db.close()

        logging.debug("PUT completed")
        return "PUT EXECUTED"
    except Exception as e:
        logging.error(f"Error in PUT: {e}")
        return "PUT ERROR", 500


@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    logging.debug(f"DELETE /employees/{id} called")
    try:
        db = get_db()
        cursor = db.cursor()

        sql = "DELETE FROM employees WHERE id=%s"
        logging.debug(f"Executing DELETE: {sql}")

        cursor.execute(sql, (id,))
        db.commit()
        db.close()

        logging.debug("DELETE completed")
        return "DELETE EXECUTED"
    except Exception as e:
        logging.error(f"Error in DELETE: {e}")
        return "DELETE ERROR", 500

@app.route("/employees/inner-join", methods=["GET"])
def inner_join():
    logging.debug("GET /employees/inner called")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        sql = """
        SELECT e.id AS employee_id, e.name AS employee_name, e.role, e.salary,
       d.dep_id, d.name AS department_name, d.location
FROM employees e
INNER JOIN departments d ON e.id = d.id;
        """
        logging.debug(f"Executing INNER JOIN: {sql}")
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in INNER JOIN: {e}")
        return "INNER JOIN ERROR", 500


@app.route("/employees/left-join", methods=["GET"])
def left_join():
    logging.debug("GET /employees/left called")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        sql = """
        SELECT e.id AS employee_id, e.name AS employee_name, e.role, e.salary,
       d.dep_id, d.name AS department_name, d.location
FROM employees e
LEFT JOIN departments d ON e.id = d.id;
        """
        logging.debug(f"Executing LEFT JOIN: {sql}")
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in LEFT JOIN: {e}")
        return "LEFT JOIN ERROR", 500


@app.route("/employees/right", methods=["GET"])
def right_join():
    logging.debug("GET /employees_departments/right called")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        sql = """
        SELECT e.id AS employee_id, e.name AS employee_name, e.role, e.salary,
       d.dep_id, d.name AS department_name, d.location
FROM employees e
RIGHT JOIN departments d ON e.id = d.id;
        """
        logging.debug(f"Executing RIGHT JOIN: {sql}")
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in RIGHT JOIN: {e}")
        return "RIGHT JOIN ERROR", 500


@app.route("/employees/full", methods=["GET"])
def full_outer_join():
    logging.debug("GET /employees/full called")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        # MySQL doesn’t support FULL OUTER JOIN directly, so we emulate with UNION
        sql = """
        SELECT e.id AS employee_id, e.name AS employee_name, e.role, e.salary,
       d.dep_id, d.name AS department_name, d.location
FROM employees e
LEFT JOIN departments d ON e.id = d.id
UNION
SELECT e.id AS employee_id, e.name AS employee_name, e.role, e.salary,
       d.dep_id, d.name AS department_name, d.location
FROM employees e
RIGHT JOIN departments d ON e.id = d.id;
        """
        logging.debug(f"Executing FULL OUTER JOIN (via UNION): {sql}")
        cursor.execute(sql)
        rows = cursor.fetchall()
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(f"Error in FULL OUTER JOIN: {e}")
        return "FULL OUTER JOIN ERROR", 500

if __name__ == "__main__":
    logging.debug("Starting Flask server...")
    app.run(debug=True)