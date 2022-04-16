from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField, SelectField
from wtforms.validators import DataRequired, optional
from wtforms_sqlalchemy.fields import QuerySelectField

from holiday_studio.models import Order, create_session


def get_all_orders():
    session = create_session()
    orders = session.query(Order).all()
    return orders


class EditOrderForm(FlaskForm):
    choice = QuerySelectField("Order", query_factory=get_all_orders, get_pk=lambda x: x.id, get_label=lambda x: x.title)
    price = FloatField("Цена заказа", validators=[DataRequired()])
    title = StringField("Название заказа", validators=[DataRequired()])
    describtion = StringField("Описание заказа", validators=[DataRequired()])
    submit = SubmitField("Создать")
