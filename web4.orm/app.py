from flask import Flask
from models.db_session import create_session, global_init


app = Flask(__name__)
app.config["SECRET_KEY"] = 'lyceum1perm'


def main():
    global_init("sqlite:///db/blogs.db")
    app.run()


if __name__ == "__main__":
    main()