from flask import Flask, jsonify, request

app=Flask(__name__)

employees=[
    {"id": 1, "name": "John", "salary": 40000},
    {"id": 2, "name": "Anita", "salary": 55000}
]

@app.get('/employees')
def get_employee():
    return jsonify(employees)


@app.post('/employees')
def add_employee():
    data = request.json
    new_e= {"id": employees[-1]["id"]+1 if employees else 1, "name": data['name'], "salary": data["salary"]}
    employees.append(new_e)
    return "Employee added"


@app.put('/employees/<int:id>')
def update_employee(id):
    data = request.json
    for emp in employees:
        if emp["id"] == id:
            emp["name"] = data.get('name', emp["name"])
            emp["salary"] = data.get('salary', emp["salary"])
            return "Employee updated"
    return "Employee not found"

@app.delete('/employees/<int:id>')
def delete_employee(id):
    for emp in employees:
        if emp["id"] == id:
            employees.remove(emp)
            return "Employee deleted"
    return "Employee not found"

if __name__ == '__main__':
    app.run(debug=True)