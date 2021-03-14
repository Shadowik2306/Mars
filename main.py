from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def title():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def song():
    return 'И на Марсе будут яблони цвести!'

@app.route('/image_mars')
def img_mars():
    return f'''<h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='mars.jpg')}"
                alt="здесь должна была быть картинка, но не нашлась"
                height=250px width=500px>'''

@app.route('/promotion_image')
def promotion_image():
    return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Колонизация</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
                integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
                <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" type="text/css">
        </head>
        <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='img/mars.jpg')}"
                    alt="здесь должна была быть картинка, но не нашлась"
                    height=250px width=500px>
                <div class="alert alert-primary" role="alert">
                      Человечество вырастает из дерева
                </div>
                <div class="alert alert-secondary" role="alert">
                      Человечеству мала одна планета
                </div>
                <div class="alert alert-success" role="alert">
                      Мы сдлеаем обитаемыми безжизненные пока планеты
                </div>
                <div class="alert alert-danger" role="alert">
                      И начнем с марса
                </div>
                <div class="alert alert-warning" role="alert">
                      Присоединяйся
                </div>
        </body>
        </html>
    '''


@app.route('/astronaut_selection')
def astronaut_selection():
    return f'''<!DOCTYPE html>
        <html lang="ru">
        <head>
            <title></title>
            <meta charset="utf-8">
            <link rel="stylesheet"
                  href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
                  integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
                  crossorigin="anonymous">
            <link rel="stylesheet" href="{url_for('static', filename='css/static/css/stile_for_find_astr.css')}">
        </head>
        <body>
            <div class="astrounaut">
                <h1>Анкета претендента</h1>
                <p>на участие в миссии</p>
                <div class="menu">
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите фамилию">
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите имя">
                    <br>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите адрес почты">
                    <div class="form-group">
                        <label for="classSelect">Какое у вас образование</label>
                        <select class="form-control" id="classSelect" name="class">
                            <option>Начальное</option>
                            <option>Среднее</option>
                            <option>Проф</option>
                            <option>Другоет</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Какие у вас есть профессии?</label>
                        <div class="form-check">
                            <input class='form-check-input' 
                            type="checkbox" name="work" value="eng">
                                <label for="eng" class="form-check-label">инженер-исследователь</label>
                        </div>
                        <div class="form-check">
                            <input class='form-check-input' 
                            type="checkbox" name="work" value="pil">
                                <label for="pil" class="form-check-label">пилот</label>
                        </div>
                        <div class="form-check">
                            <input class='form-check-input' 
                            type="checkbox" name="work" value="build">
                                <label for="build" class="form-check-label">строитель</label>
                        </div>
                        <div class="form-check">
                            <input class='form-check-input' 
                            type="checkbox" name="work" value="bio">
                                <label for="bio" class="form-check-label">экзобиолог</label>
                        </div>
                        <div class="form-check">
                            <input class='form-check-input' 
                            type="checkbox" name="work" value="doc">
                                <label for="doc" class="form-check-label">врач</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="form-check">Укажите пол</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                <label class="form-check-label" for="male">
                                    Мужской
                                </label>
                            </div>
                            <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                <label class="form-check-label" for="female">
                                    Женский
                                </label>
                            </div>
                    </div>
                    <div class="form-group">
                        <label>Почему вы хотите принять участие?</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="photo">Приложите фотографию</label>
                        <input type="file" class="form-control-file" id="photo" name="file">
                    </div>
                    <div class="form-group">
                        <div class="form-check">
                            <input class='form-check-input' 
                            type="checkbox" name="ready" value="agree">
                                <label for="agree" class="form-check-label">Готовы остаться на Марсе?</label>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </div>
            </div>
        </body>
        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
