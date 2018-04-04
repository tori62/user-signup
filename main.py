from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/welcome", methods=['POST'])
def response():
    name = request.form['username']
    word = request.form['password']
    verify = request.form['verify_password']
    
    if name == "":
        name_error = "Please enter a username"
        return render_template('index.html' password=word verify_password= verify name_error=name_error)

    elif word == "":
        word_error = "Please enter a password"
        return render_template('index.html' password=word_error)

    elif verify == "":
        verify_error = "Please verify password"
        return render_template('index.html' verify_password=verify_error)

    else:
        return render_template('welcome.html', username=name)



app.run()
