from flask import Flask
from models.db_session import create_session, global_init
from routers import employee_router


app = Flask(__name__)
app.config["SECRET_KEY"] = 'lyceum1perm'
app.register_blueprint(employee_router)



def main():
    global_init("sqlite:///../db/holiday.db")
    app.run()

if __name__ == "__main__":
    main()