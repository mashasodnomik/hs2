from flask import Blueprint, request
from models import AlchemyEncoder
from models import Employee, create_session
import json


router = Blueprint("employee_api",
                   __name__,
                   template_folder="/server/templates",
                   url_prefix="/employee")


@router.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    session = create_session()
    employee = session.query(Employee).get(employee_id)  # аналогично session.query(Employee).where(Employee.id == employee_id)
    if employee:
        result = json.dumps(employee, cls=AlchemyEncoder, ensure_ascii=False)
    else:
        result = json.dumps(None)
    session.close()
    return result


@router.route("/", methods=["GET"])
def get_employees():
    session = create_session()
    employees = session.query(Employee).all()
    result = json.dumps(employees, cls=AlchemyEncoder, ensure_ascii=False)
    session.close()
    return result


@router.route("/", methods=["POST"])
def create_employee():
    session = create_session()
    json_data = request.json
    new_employee = Employee(**json_data)
    session.add(new_employee)
    session.commit()
    result = json.dumps(new_employee, cls=AlchemyEncoder, ensure_ascii=False)
    session.close()
    return result


@router.route("/<int:employee_id>", methods=["PUT"])
def put_employee(employee_id):
    session = create_session()
    employee = session.query(Employee).get(employee_id)  # аналогично session.query(Employee).where(Employee.id == employee_id)
    if employee:
        json_data = request.json  # пример: {"fullname": "Роман", login: "grm"} - означает, что нужно изменить только 2 поля. Как распарсить?
        """
        можно так (деревенский подход): проблема подхода, что для каждого поля надо проверять, есть ли оно в json_data
        >>>
        if "full_name" in json_data:
            employee.full_name = json_data["fullname"]
        if "email" in json_data:
            employee.email = json_data["email"]
        if "login" in json_data:
            employee.login = json_data["login"]
        if "password" in json_data:
            employee.password = json_data["password"]
        if "phone" in json_data:
            employee.phone = json_data["phone"]
        <<<
        """
        # лучше:
        for key, value in json_data.items():
            setattr(employee, key, value)  # задаем в employee полю key значение value
        session.commit()
        result = json.dumps(employee, cls=AlchemyEncoder, ensure_ascii=False)
    else:
        result = json.dumps({})
    session.close()
    return result


@router.delete("/<int:employee_id>")
def delete_employee(employee_id):
    session = create_session()
    employee = session.query(Employee).get(employee_id)  # аналогично session.query(Employee).where(Employee.id == employee_id)
    if employee:
        session.delete(employee)
        session.commit()
        result = json.dumps(True)
    else:
        result = json.dumps(False)
    session.close()
    return result
