from flask import Blueprint, request, render_template

from forms.login import LoginForm
from models import AlchemyEncoder
from models import Order, create_session
import json


router = Blueprint("site",
                   __name__,
                   template_folder="/server/templates",
                   url_prefix="/site")


@router.route("/login")
def login():
    login_form = LoginForm()
    render_template("login.html", title="Авторизация", form=login_form)