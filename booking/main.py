from flask import Flask
from server.data import db_session
from booking import rest_bp

app = Flask(__name__)

db_session.global_init("../server/data/db/cinema.db")

SECRET_KEY = 'yandexlyceum_secret_key'


app.config['SECRET_KEY'] = SECRET_KEY


is_authorized = False


if __name__ == '__main__':
    app.register_blueprint(rest_bp.blueprint)
    app.run(port=8080, host='127.0.0.1')
