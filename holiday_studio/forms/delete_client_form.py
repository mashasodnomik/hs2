from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from holiday_studio.models import create_session
from holiday_studio.models.client import Client


def get_names():
    session = create_session()
    names = session.query(Client).all()
    session.close()
    return names


class DeleteClientForm(FlaskForm):
    choice = QuerySelectField("Выберите кого удалить", query_factory=get_names, get_pk=lambda x: x.id, get_label=lambda x: x.full_name)
    submit = SubmitField("Удалить")