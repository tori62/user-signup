from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/login")
def index():
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def response():
    name = request.form['username']
    word = request.form['password']
    verify = request.form['verify_password']
    
    if name == "":
        error = "Please enter a username"
        username=''
        return render_template('index.html', username=username, name_error=error)

    elif word == "":
        error = "Please enter a password"
        return render_template('index.html', username=name, word_error=error)

    elif verify != word:
        error = "The password does not match, please re-enter"
        return render_template('index.html', username=name, password=word, verify_error=error)

    else:
        return render_template('welcome.html', username=name)


app.run()
