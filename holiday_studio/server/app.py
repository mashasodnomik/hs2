from flask import Flask
from flask_login import LoginManager

from models import global_init
from routers import employee_router, order_router, page_router


app = Flask(__name__)
app.config["SECRET_KEY"] = 'lyceum1perm'
app.register_blueprint(employee_router)
app.register_blueprint(order_router)
app.register_blueprint(page_router)
login_manager = LoginManager()
login_manager.init_app(app)


def run_server(port=5000, host="127.0.0.1"):
    global_init("sqlite:///../database/holiday.db")
    app.run(host=host, port=port)


if __name__ == "__main__":
    run_server()
