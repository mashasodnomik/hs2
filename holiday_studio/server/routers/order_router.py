from flask import Blueprint, request
from models import AlchemyEncoder
from models import Order, create_session
import json


router = Blueprint("order_api",
                   __name__,
                   template_folder="/server/templates",
                   url_prefix="/order")


@router.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    session = create_session()
    order = session.query(Order).get(order_id)  # аналогично session.query(Order).where(order.id == order_id).first()
    if order:
        result = json.dumps(order, cls=AlchemyEncoder, ensure_ascii=False)
    else:
        result = json.dumps(None)
    session.close()
    return result


@router.route("/", methods=["GET"])
def get_orders():
    session = create_session()
    orders = session.query(Order).all()
    result = json.dumps(orders, cls=AlchemyEncoder, ensure_ascii=False)
    session.close()
    return result


@router.route("/", methods=["POST"])
def create_order():
    session = create_session()
    json_data = request.json
    new_order = Order(**json_data)
    session.add(new_order)
    session.commit()
    result = json.dumps(new_order, cls=AlchemyEncoder, ensure_ascii=False)
    session.close()
    return result


@router.route("/<int:order_id>", methods=["PUT"])
def put_order(order_id):
    session = create_session()
    order = session.query(Order).get(order_id)  # аналогично session.query(Order).where(order.id == order_id)
    if order:
        json_data = request.json  # пример: {"fullname": "Роман", login: "grm"} - означает, что нужно изменить только 2 поля. Как распарсить?
        """
        можно так (деревенский подход): проблема подхода, что для каждого поля надо проверять, есть ли оно в json_data
        >>>
        if "full_name" in json_data:
            order.full_name = json_data["fullname"]
        if "email" in json_data:
            order.email = json_data["email"]
        if "login" in json_data:
            order.login = json_data["login"]
        if "password" in json_data:
            order.password = json_data["password"]
        if "phone" in json_data:
            order.phone = json_data["phone"]
        <<<
        """
        # лучше:
        for key, value in json_data.items():
            setattr(order, key, value)  # задаем в order полю key значение value
        session.commit()
        result = json.dumps(order, cls=AlchemyEncoder, ensure_ascii=False)
    else:
        result = json.dumps(None)
    session.close()
    return result


@router.delete("/<int:order_id>")
def delete_order(order_id):
    session = create_session()
    order = session.query(Order).get(order_id)  # аналогично session.query(Order).where(order.id == order_id)
    if order:
        session.delete(order)
        session.commit()
        result = json.dumps(True)
    else:
        result = json.dumps(False)
    session.close()
    return result
