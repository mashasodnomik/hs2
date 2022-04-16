from os import abort
import sqlalchemy
from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError
from holiday_studio.forms.create_client import CreateClientForm
from holiday_studio.forms.create_order import CreateOrderForm
from holiday_studio.forms.login import LoginForm
from holiday_studio.forms.delete_client_form import DeleteClientForm
from holiday_studio.forms.delete_order_form import DeleteOrderForm
from holiday_studio.models import AlchemyEncoder, Employee, Client, EmployeeOrder, ClientOrder
from holiday_studio.models import Order, create_session
from holiday_studio.forms.edit_client_form import EditClientForm
from holiday_studio.forms.edit_order_form import EditOrderForm
from flask_login import current_user

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
            session.close()
            return redirect("/")
        else:
            session.close()
            return redirect("/site/login")
    return render_template("login.html", title="Авторизация", form=login_form)


@router.route("/create_client", methods=["GET", "POST"])
@login_required
def create_client():
    create_client_form = CreateClientForm()
    if create_client_form.validate_on_submit():
        session = create_session()
        client = Client(full_name=create_client_form.full_name.data,
                        age=create_client_form.age.data,
                        phone=create_client_form.phone.data,
                        email=create_client_form.email.data)
        session.add(client)
        try:
            session.commit()
            session.close()
            return redirect("/")
        except IntegrityError:
            create_client_form.email.errors.append("Email уже используется")
            session.close()
            return render_template("create_client.html", title="Создание клиента", form=create_client_form)

    return render_template("create_client.html", title="Создание клиента", form=create_client_form)


@router.route("/create_order", methods=["GET", "POST"])
@login_required
def create_order():
    create_order_form = CreateOrderForm()
    if create_order_form.validate_on_submit():
        client = create_order_form.client_list.data
        session = create_session()
        order = Order(price=create_order_form.price.data,
                      title=create_order_form.title.data,
                      describtion=create_order_form.describtion.data)
        # чтобы получить order_id сначала добавим в базу
        session.add(order)
        session.commit()

        # связываем M:M
        employee_order = EmployeeOrder(id_employee=current_user.id,
                                       id_order=order.id)
        client_order = ClientOrder(id_client=client.id,
                                   id_order=order.id)

        session.add(client_order)
        session.add(employee_order)
        session.commit()
        session.close()
        return redirect("/")
    return render_template("create_order.html", title="Создание заказа", form=create_order_form)


@router.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@router.route("/all_clients", methods=["GET", "POST"])
@login_required
def all_clients():
    session = create_session()
    results = list(map(lambda x: x.full_name, session.query(Client).all()))
    session.close()
    return render_template("clients.html", clients=results)


@router.route("/all_orders", methods=["GET", "POST"])
@login_required
def all_orders():
    results = []
    session = create_session()
    orders = list(map(lambda x: session.query(Order).filter(Order.id == x.id_order).first(),
                      session.query(EmployeeOrder).filter(EmployeeOrder.id_employee == current_user.id).all()))
    for x in orders:
        if x is not None:
            results.append(x.title)
    session.close()
    return render_template("orders.html", orders=results)


@router.route("/delete_client", methods=["GET", "POST"])
@login_required
def delete_client():
    form = DeleteClientForm()
    if form.validate_on_submit():
        deleted_client = form.choice.data
        current_session = create_session()
        current_session.delete(deleted_client)
        current_session.commit()
        current_session.close()
        return redirect("/")
    return render_template("delete_client.html", title="удаление клиента", form=form)


@router.route("/delete_order", methods=["GET", "POST"])
@login_required
def delete_order():
    form = DeleteOrderForm()
    if form.validate_on_submit():
        current_session = create_session()
        deleted_order = form.choice.data
        deleted_emplord = current_session.query(EmployeeOrder).filter(EmployeeOrder.id_order == deleted_order.id).first()
        deleted_clienord = current_session.query(ClientOrder).filter(ClientOrder.id_order == deleted_order.id).first()
        if deleted_order:
            current_session.delete(deleted_emplord)
            current_session.delete(deleted_clienord)
            current_session.delete(deleted_order)
        current_session.commit()
        current_session.close()
        return redirect("/")
    return render_template("delete_order.html", title="удаление заказа", form=form)


@router.route("/edit_client", methods=["GET", "POST"])
@login_required
def edit_client():
    edit_client_form = EditClientForm()
    session = create_session()
    edited_client = edit_client_form.choice.data
    if edit_client_form.validate_on_submit():
        edited_client.full_name = edit_client_form.new_name.data
        edited_client.age = edit_client_form.age.data
        edited_client.phone = edit_client_form.phone.data
        edited_client.email = edit_client_form.email.data
        session.commit()
        session.close()
        return redirect('/')
    return render_template("edit_client.html", title="Изменение клиента", form=edit_client_form)








