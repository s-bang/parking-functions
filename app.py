from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World! Welcome to the site! Goodbyte Cruel World!</h1>"


if __name__ == '__main__':
    app.run()
