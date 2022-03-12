from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, logout_user, login_required

from forms.create_client import CreateClientForm
from forms.login import LoginForm
from models import AlchemyEncoder, Employee
from models import Order, create_session
import json
# from flask_login import current_user

router = Blueprint("",
                   __name__,
                   template_folder="/server/templates")


@router.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session = create_session()
        employee = session.query(Employee).\
            filter(Employee.email == login_form.email.data).first()
        if employee and employee.check_password(login_form.password.data):
            login_user(employee)
            return redirect("/")
        else:
            return redirect("/site/login")
    return render_template("login.html", title="Авторизация", form=login_form)


@router.route("/create_client", methods=["GET", "POST"])
@login_required
def create_client():
    create_client_form = CreateClientForm()
    if create_client_form.validate_on_submit():
        pass
        """
        session = create_session()
        employee = session.query(Employee).\
            filter(Employee.email == login_form.email.data).first()
        if employee and employee.check_password(login_form.password.data):
            login_user(employee)
            return redirect("/")
        else:
            return redirect("/site/login")
        """
    return render_template("create_client.html", title="Создание клиента", form=create_client_form)


@router.route("/logout")
def logout():
    logout_user()
    return redirect("/")
