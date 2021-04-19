from flask import Flask
from .data import db_session
from .data.tabels.seanses import Seanse
from .data.tabels.rooms import Room
from .data.tabels.users import User
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("data/db/cinema.db")


def add_user(name, email, password):
    user = User()
    user.name = name
    user.email = email
    user.password = password
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def bron_sides(id, sides):
    dict = {}

    with open("../booking/halls/" + id, "rt", encoding="utf8") as f:
        places = json.loads(f.read())
        places = places['places']
    for x, y in sides:
        places[y][x] = 1
    dict['places'] = places
    print(places)
    with open("../booking/halls/" + id, "w", encoding="utf8") as f:
        json.dump(dict, f, ensure_ascii=False)

def log_in(name, password):
    data = []
    db_sess = db_session.create_session()
    for user in db_sess.query(User).all():
        data.append((user.name, user.password))
    for namex, passwordx in data:
        if namex == name:
            if passwordx == password:
                return '0'
            else:
                return 'Неверный пароль'
    return 'Неверное имя пользователя'


def register(name, email, password):
    names = []
    emails = []
    db_sess = db_session.create_session()
    for user in db_sess.query(User).all():
        names.append(user.name)
        emails.append(user.email)
    for namex in names:
        if namex == name:
            return 'Имя пользователя занято'
    for emailx in emails:
        if emailx == email:
            return 'Почта занята'
    add_user(name, email, password)
    return '0'


def get_films():
    films = []
    inform = {}
    response = {}
    db_sess = db_session.create_session()
    for film in db_sess.query(Seanse).all():
        inform['info'] = ', '.join([film.name, str(film.date), str(film.time), str(film.cost),
                                    film.room_name, str(film.sides_left)])
        films.append(inform)

    response['films'] = films
    with open('films.json', 'w', encoding="utf-8") as file:
        json.dump(response, file, ensure_ascii=False)


def add_room(name, capacity):
    room = Room()
    room.name = name
    room.capacity = capacity
    db_sess = db_session.create_session()
    db_sess.add(room)
    db_sess.commit()


def add_session(name, date, time, room_name, cost, sides_left):
    session = Seanse()
    session.name = name
    session.date = date
    session.time = time
    session.cost = cost
    session.room_name = room_name
    session.sides_left = sides_left

    session.room_name = room_name
    db_sess = db_session.create_session()
    db_sess.add(session)
    db_sess.commit()


def main():
    print(log_in('name3', 'password5'))


if __name__ == '__main__':
    main()
