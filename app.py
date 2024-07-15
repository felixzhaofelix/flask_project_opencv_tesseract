from flask import Flask, render_template, redirect, request, url_for, session, flash
import utils

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    header = 'Home'
    return render_template("index.html", header=header)


@app.route('/upload/')
def upload():
    header = 'Upload'
    return render_template("upload.html", header=header)


@app.route('/search/')
def search():
    header = 'Search'
    return render_template("Search.html", header=header)


@app.route('/greeting/<user>')
def greeting(user):
    greeting = f'hello {user}'
    return render_template("index.html", greeting=greeting)


@app.route('/get_image/')
def get_image():
    return "static/img/emoji1.png"


@app.route('/scripts/script.js/')
def get_script():
    return "templates/scripts/script.js"


if __name__ == '__main__':
    app.run(debug=True)
