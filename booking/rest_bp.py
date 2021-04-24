import json

import flask
from checker import check_correct
from server import Handler
from flask import render_template, request, redirect

from booking.loginform import LoginForm
from booking.user import RegisterForm
# from server.Handler import bron_sides
from server.Handler import bron_sides
from server.data import db_session
from server.data.tabels.users import User
from .main import is_authorized

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        ans = Handler.register(form.name.data, form.email.data, form.password.data)
        if ans == "0":
            return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ans = Handler.log_in(form.username.data, form.password.data)
        if ans == "0":
            return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@blueprint.route('/seanses', methods=['GET', 'POST'])
def seanses():
    if is_authorized:
        return render_template("seanses.html")
    else:
        return login()


@blueprint.route('/process_data/<id>', methods=['GET', 'POST'])
def process_data(id):
    id = int(id)
    bron_sides("places_first_hall.json", [(id % 11, id // 8)])
    return redirect("/choice/1")


@blueprint.route('/success')
def success():
    global is_authorized
    is_authorized = True
    return f"""<head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <title>Успешная авторизация</title>
        </head><h2 align="center">
        <div class="alert alert-info" role="alert">Вход в аккаунт выполнен!</div></h2>
        <div class="col text-center"><button type="button" class="btn btn-warning" >
        <a href="/"><h3>Вернуться на главную</h3></a></button></div>"""


@blueprint.route('/')
@blueprint.route('/index')
def index():
    Handler.get_films()
    with open("../server/films.json", "rt", encoding="utf8") as f:
        films_list = json.loads(f.read())
    print(films_list)
    return render_template('site.html', films=films_list)


@blueprint.route('/choice/<int:quantity>', methods=['POST', "GET"])
def choice(quantity):
    with open("halls/places_first_hall.json", "rt", encoding="utf8") as js:
        matrix = json.loads(js.read())["places"]
    param = {}
    param["matrix"] = matrix
    param["quantity"] = quantity
    param["check_correct"] = check_correct
    return render_template("choice.html", **param)


@blueprint.route('/f', methods=['POST'])
def f():
    requests = int(request.form['A'])
    result = check_correct(requests)
    if result == 1:
        return """<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <title>Ошибка</title>
    </head><h2 align="center">
    <div class="alert alert-danger" role="alert">Неккоректный ввод</div></h2>"""
    else:
        return f"""<head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <title>Забронированый билет</title>
        </head><h2 align="center">
        <div class="alert alert-info" role="alert">Вы успешно забронировали {result}!</div></h2>
        <div class="col text-center"><button type="button" class="btn btn-warning" >
        <a href="/"><h3>Вернуться на главную</h3></a></button></div>
        <div class="col text-center"><button type="button" class="btn btn-warning" >
        <a href="/choice/{int(result.split()[0])}"><h3>Выбрать места</h3></a></button></div>"""
