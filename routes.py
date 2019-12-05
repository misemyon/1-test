from flask import Blueprint, jsonify

from models import Employee, db

index = Blueprint('index', __name__, url_prefix='/')
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/employees')
def get_employees():
    return jsonify([(lambda men: men.json())(men) for men in Employee.query.all()])

@api.route('/employee/id/<int:men_id>')
def get_employee(men_id):
    employee = Employee.query.get(men_id)
    return jsonify(employee.json()) if employee else ''


@api.route('/employee/name/<string:employee_name>')
def put_men(employee_name, pn):
    employee = Employee(name=employee_name)
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee.json())

@index.route('/')
@index.route('/index')
def get_index():
    return '''
            <html>
                <title>
                    Mega RESTful web service
                </title>
                <body>
                    <h3>API:</h3>
                    <a href="./api/employees">Employee</a>
                </body>
            </html>
           '''
