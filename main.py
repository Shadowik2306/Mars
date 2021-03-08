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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
