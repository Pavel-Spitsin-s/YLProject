from flask import Flask
from data import db_session
from data.tabels.seanses import Seanse
from data.tabels.rooms import Room
from data.tabels.viewers import Viewer
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("data/db/cinema.db")


def add_viewer(name, email, cancel_code, session_id):  # test commit from home
    viewer = Viewer()
    viewer.name = name
    viewer.email = email
    viewer.cancel_code = cancel_code
    viewer.session_id = session_id
    db_sess = db_session.create_session()
    db_sess.add(viewer)
    db_sess.commit()


def get_films():
    films = []
    db_sess = db_session.create_session()
    for film in db_sess.query(Seanse).all():
        infor = {}
        infor['info'] = ', '.join([film.name, str(film.date), str(film.time), str(film.cost), film.room_name])
        films.append(infor)
    response = {}
    response['films'] = films
    with open('films.json', 'w') as file:
        json.dump(response, file, ensure_ascii=False)


def add_room(name, capacity):
    room = Room()
    room.name = name
    room.capacity = capacity
    db_sess = db_session.create_session()
    db_sess.add(room)
    db_sess.commit()


def add_session(name, date, time, room_name, cost):
    session = Seanse()
    session.name = name
    session.date = date
    session.time = time
    session.cost = cost
    session.room_name = room_name

    session.room_name = room_name
    db_sess = db_session.create_session()
    db_sess.add(session)
    db_sess.commit()


def main():
    get_films()


if __name__ == '__main__':
    main()
    app.run()
