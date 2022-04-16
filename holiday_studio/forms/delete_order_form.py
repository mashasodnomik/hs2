from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from holiday_studio.models import create_session
from holiday_studio.models.employee_order import EmployeeOrder
from holiday_studio.models.order import Order
from flask_login import current_user


def get_orders():
    session = create_session()
    orders = list(map(lambda x: session.query(Order).filter(Order.id == x.id_order).first(),
                      session.query(EmployeeOrder).filter(EmployeeOrder.id_employee == current_user.id).all()))
    session.close()
    return orders


class DeleteOrderForm(FlaskForm):
    choice = QuerySelectField("Выберите что удалить", query_factory=get_orders, get_pk=lambda x: x.id,
                              get_label=lambda x: x.title)
    submit = SubmitField("Удалить")