import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/odd_even/<int:number>')
def odd_even(number):
    return render_template('odd_even.html', number=number)


@app.route('/news')
def news():
    with open("news.json", "r", encoding="utf-8") as f:
        news_list = json.load(f)
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route("/queue")
def queue():
    return render_template("queue.html", title="Очередь")


@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        return render_template("training.html",
                               title="Тренировка",
                               training_name="Инженерные тренажеры",
                               path_to_image=url_for("static",
                                                     filename="img/Инженерные тренажеры.jpg"))
    else:
        return render_template("training.html",
                               title="Тренировка",
                               training_name="Научные симуляторы",
                               path_to_image=url_for("static",
                                                     filename="img/Научные симуляторы.jpg"))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')