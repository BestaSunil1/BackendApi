# BackendApi
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

# Employee Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.String, nullable=False)
    emp_name = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    city = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

# Create an employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee = Employee(**data)
    db.session.add(employee)
    db.session.commit()
    return jsonify({'id': employee.id})

# Get employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify(employee.__dict__)

# Update employee by ID
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    data = request.json
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify({'message': 'Employee updated'})

# Delete employee by ID
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

