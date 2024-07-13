from flask import Flask, render_template
import project

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    num = 10
    return render_template("index.html", num=num)


@app.route('/small/')
def display_small():
    project.run_small()




if __name__ == '__main__':
    app.run()
