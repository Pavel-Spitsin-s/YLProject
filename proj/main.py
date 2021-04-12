from flask import Flask
from data import db_session
from data.seanses import Session
from data.visitors import Viewers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/cinema.db")

def main():
    Viewer = Viewers()
    Viewer.name = "Пользователь 1"
    Viewer.email = "email@email.ru"
    Viewer.cancel_code = 'adasdas'
    Viewer.film_id = 123456
    db_sess = db_session.create_session()
    db_sess.add(Viewer)
    db_sess.commit()
    print(0)

if __name__ == '__main__':
    main()
    app.run()
