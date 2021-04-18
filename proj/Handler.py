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
    viewer.cancel_codse = cancel_code
    viewer.session_id = session_id
    db_sess = db_session.create_session()
    db_sess.add(viewer)
    db_sess.commit()


def bron_sides(id, sides):
    with open("../booking/halls/" + id, "rt", encoding="utf8") as f:
        places = json.loads(f.read())
        places = places['places']
    for x, y in sides:
        places[y][x] = 1
    dict = {}
    dict['places'] = places
    with open("../booking/halls/" + id, "w", encoding="utf8") as f:
        json.dump(dict, f, ensure_ascii=False)


def is_full(film_id, capacity):
    pass


def get_films():
    films = []
    db_sess = db_session.create_session()
    for film in db_sess.query(Seanse).all():
        infor = {}
        infor['info'] = ', '.join([film.name, str(film.date), str(film.time), str(film.cost),
                                   film.room_name, str(film.sides_left)])
        films.append(infor)
    response = {}
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
    bron_sides('places_first_hall.json', [(0, 5), (1, 0), (3, 0), (2, 0)])


if __name__ == '__main__':
    main()
