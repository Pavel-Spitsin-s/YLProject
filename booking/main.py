import json
# from proj import Handler
from flask import Flask, render_template, request

app = Flask(__name__)
R_PAD = [2, 3, 4]
M_FORM = [5, 6, 7, 8, 9, 0]


def check_correct(num):
    try:
        num = int(num)
        if num < 1:
            return 1
        elif num % 10 == 1:
            return str(num) + " место"
        elif num % 10 in R_PAD:
            return str(num) + " места"
        elif num % 10 in M_FORM and num != 0:
            return str(num) + " мест"
        else:
            return 1
    except Exception:
        return 1


@app.route('/')
@app.route('/index')
def index():
    # Handler.main()
    with open("films.json", "rt", encoding="utf8") as f:
        films_list = json.loads(f.read())
    print(films_list)
    return render_template('site.html', films=films_list)


@app.route('/f', methods=['POST'])
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
        <a href="/"><h3>Вернуться на главную</h3></a></button></div>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
