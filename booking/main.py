from flask import Flask

from booking import rest_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


is_authorized = False


if __name__ == '__main__':
    app.register_blueprint(rest_bp.blueprint)
    app.run(port=8080, host='127.0.0.1')
