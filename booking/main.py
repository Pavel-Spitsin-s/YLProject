import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    with open("films.json", "rt", encoding="utf8") as f:
        films_list = json.loads(f.read())
    print(films_list)
    return render_template('site.html', films=films_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')