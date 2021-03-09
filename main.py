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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
