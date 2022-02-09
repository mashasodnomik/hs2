import json

from flask import Flask, render_template, url_for, redirect
from dotenv import load_dotenv
import os
from forms.loginform import LoginForm
from forms.crash_loginform import CrashLoginForm


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("MY_SECRET_KEY")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/crash_login", methods=['GET', 'POST'])
def crash_login():
    form = CrashLoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('crash_login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')