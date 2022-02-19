from flask import Blueprint, request

from models.code_gen import Employee
from models.db_session import create_session
import json


router = Blueprint("employee_api",
                   __name__,
                   template_folder="/server/templates",
                   url_prefix="/employee")


@router.route("/", methods=["GET"])
def get_employees():
    with create_session() as session:
        employees = session.query(Employee).all()
        result = list(map(lambda x: x.__dict__, employees))
        return json.dumps(result)


@router.route("/", methods=["POST"])
def create_employee():
    with create_session() as session:
        json_data = request.json
        new_employee = Employee(**json_data)
        session.add(new_employee)
        session.commit()
        return json.dumps(new_employee.__dict__)
