from flask import Flask
from data import db_session
from data.tabels.seanses import Seanse
from data.tabels.rooms import Room
from data.tabels.viewers import Viewer
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


def add_room(name, capacity):
    room = Room()
    room.name = name
    room.capacity = capacity
    db_sess = db_session.create_session()
    db_sess.add(room)
    db_sess.commit()


def add_session(name, date, time, room_name, cancel_code, session_id):
    session = Seanse()
    session.name = name
    session.date = date
    session.time = time
    session.room_name = room_name
    session.cancel_code = cancel_code
    session.session_id = session_id
    db_sess = db_session.create_session()
    db_sess.add(session)
    db_sess.commit()


def main():
    add_viewer("Пользователь 1", "eml@email.ru", 'C1A2NC3', 512313)
    add_room('superoom', 25)
    add_session('Гадза против макаки', datetime.date(2021, 5, 12), datetime.time(15, 00), 'superoom', 'D1251E', 1)


if __name__ == '__main__':
    main()
    app.run()
