import os

from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
import utils
import example


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'a_secret_key'


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/get_available_files/')
def get_available_files():

    if session.get('username') is None:
        flash('You need to log in first.')
        return jsonify({'message': 'You are not logged in!'})

    user_directory_path = os.path.join(app.config['UPLOAD_FOLDER'], session.get('username'))

    if not os.path.isdir(user_directory_path):
        flash('No file found for this user.')
        return jsonify({'message': 'No file found for this user.'})

    else:
        files = {}
        for filename in os.listdir(user_directory_path):
            files[filename] = os.path.join(user_directory_path, filename)
    return jsonify(files)


@app.route('/get_session/')
def get_session():
    if session:  # if session is not empty
        response = {}
        for key, value in session.items():
            response[key] = value
        return jsonify(response) # whatever I return here, is the xhr.responseText, same for all other requests
    else:  # if session is empty
        return jsonify({'error': 'Session not found'})


@app.route('/get_users/')
def get_users():
    with open('static/usernames/usernames.txt', 'r') as f:
        usernames = [readline.strip() for readline in f.readlines() if readline.strip() != '']
    return jsonify(usernames)


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()  # get username from request and strip any extra spaces

        username_file_path = 'static/usernames/usernames.txt'
        if not os.path.exists(username_file_path):  # first time creating file
            os.makedirs('static/usernames', exist_ok=True)
            with open(username_file_path, 'w') as file:
                file.write("")  # create empty file

        with open(username_file_path, 'r') as file:
            usernames = [line.strip() for line in file.readlines()]  # strip newline characters from usernames

        if username in usernames:
            is_returning_user = True
            session['username'] = username  # case where it's an existing user
            session['is_returning_user'] = is_returning_user
        else:
            session['username'] = username  # case where it's a new user
            is_returning_user = False
            session['is_returning_user'] = is_returning_user
            with open(username_file_path, 'a') as file:
                if usernames:  # if usernames is not empty
                    file.write('\n' + username)
                else:  # if usernames is empty
                    file.write(username)

        if is_returning_user:
            # flash(f'Hello again {username} from flashing')
            # session.pop('username', None)
            return jsonify({'message': session['username'], 'is_returning_user': session['is_returning_user']}), 200
        else:
            # flash(f'Hello New Visitor {username} from flashing')
            return jsonify({'message': session['username'], 'is_returning_user': session['is_returning_user']}), 200


@app.route('/upload/', methods=['POST'])
def upload():
    usr_name = str(session['username'])
    is_returning_user = bool(session['is_returning_user'])
    if request.method == 'POST':
        if 'file' not in request.files:  # if there's no file item in the request
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and file.filename.endswith('.zip'):  # if we have a valid zipfile
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], usr_name)
            os.makedirs(file_path, exist_ok=True)
            file.save(os.path.join(file_path, filename))
            return jsonify({'message': f'File uploaded successfully and saved at {file_path}'}), 200

        return 'Invalid file type', 400
    return redirect(url_for('home'))


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


@app.route('/extract_selected_file/')
def extract_selected_file():
    filename = request.args.get('filename')

    # check if user is in session, otherwise store under directory user=anonymous
    if 'username' in session:
        username = session['username']
    else:
        username = 'anonymous'

    # check if user has a directory


    # make a directory in unzippedFiles in the pattern :
    # unzippedFiles/user/zipfilename/zipfilename_faces
    # or
    # unzippedFiles/user/zipfilename/zipfilename_text

    # save in directory

    # return result message





if __name__ == '__main__':
    app.run(debug=True)
