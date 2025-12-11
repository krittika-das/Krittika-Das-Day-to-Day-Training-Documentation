from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Direct DB config
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mhdhwdh75%)&&0%',
    'database': 'todo_app',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_connection():
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC;")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    if not title.strip():
        flash("Title is required")
        return redirect(url_for('index'))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Task added successfully")
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=%s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Task marked as completed")
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        cursor.execute("UPDATE tasks SET title=%s, description=%s, status=%s WHERE id=%s",
                       (title, description, status, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Task updated")
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM tasks WHERE id=%s", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Task deleted")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=False)