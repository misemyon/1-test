from flask import Blueprint, jsonify

from models import Employee, db, Position

index = Blueprint('index', __name__, url_prefix='/')
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/employees')
def get_employees():
    return jsonify([(lambda men: men.json())(men) for men in Employee.query.all()])

@api.route('/employee/id/<int:men_id>')
def get_employee(men_id):
    employee = Employee.query.get(men_id)
    return jsonify(employee.json()) if employee else ''

@api.route('/employee/name/<string:employee_name>/pos/<int:pos_id>')
def put_men(employee_name, pos_id):
    employee = Employee(name=employee_name, position_id=pos_id)
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee.json())

@api.route('/position/name/<string:pos_name>')
def put_pos(pos_name):
    position = Position(name=pos_name)
    db.session.add(position)
    db.session.commit()
    return jsonify(position.json())

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
