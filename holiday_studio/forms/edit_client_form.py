from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TelField, EmailField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from holiday_studio.models import Client, create_session


def get_all_clients():
    session = create_session()
    clients = session.query(Client).all()
    session.close()
    return clients


class EditClientForm(FlaskForm):
    choice = QuerySelectField(QuerySelectField("Клиент", query_factory=get_all_clients,
                                   get_pk=lambda client: client.id,
                                   get_label=lambda client: client.full_name))
    new_name = SubmitField("Новое имя", validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    phone = TelField("Номер телефона", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Создать")