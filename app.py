import os

from flask import Flask, render_template, redirect, request, url_for, session, flash
import utils
import example


app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    header = 'Upload'
    return render_template("upload.html", header=header)


@app.route('/search/')
def search():
    header = 'Search'
    return render_template("Search.html", header=header)


@app.route('/describe/')
def describe():
    header = 'Describe'
    return render_template("Describe.html", header=header)



@app.route('/example/')
def example():
    return render_template("example.html")


@app.route('/get_image/')
def get_image():
    return "static/img/emoji1.png"


@app.route('/get_example_img/')
def get_example_img():
    example_src = "static/img/sample-newspaper.png"
    example_cs_path = "static/img/example_cs.png"

    # Check if the image already exists
    if not os.path.exists(example_cs_path):
        example_d = example.extract_example(example_src)
        example_cs = example.make_cs_by_size(example_d['faces'], 2, 3)
        example_cs.save("static/img/example_cs.png")

    return example_cs_path


@app.route('/get_example_text/')
def get_example_text():
    with open("static/unzippedFiles/small/small_text/small_text_0", "r") as f:
        content = f.read()
    return content


if __name__ == '__main__':
    app.run(debug=True)
