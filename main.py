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
    email = request.form['email']
    
    if name == "":
        error = "Please enter a username"
        username=''
        return render_template('index.html', username=username, name_error=error, email=email)
    else:
        if not_valid(name) == True:
            error = "Please enter a valid username (between 3-20 characters and no spaces)"
            username=''
            return render_template('index.html', username=username, name_error=error, email=email)  
    
    if word == "":
        error = "Please enter a password"
        return render_template('index.html', username=name, word_error=error, email=email)
    else:
        if not_valid(word) == True:
            error = "Please enter a valid password between 3-20 characters and no spaces"
            password = ''
            return render_template('index.html',username=name, password=password, word_error=error, email=email)

    if verify != word:
        error = "Password did not match. Please re-enter password and verify"
        return render_template('index.html', username=name, verify_error=error, email=email)

    
    if email != '': 
        if not_valid_email(email) == True:
            error = "Please enter valid email"
            email = ''
            password = ''
            verify_password = ''
            return render_template('index.html', username = name, password=password, verify_password=verify_password, email_error=error)
          
    return render_template('welcome.html', username=name)

def not_valid(name):
    for i in name:
        if i == " ":
            return True
        elif len(name) < 3 or len(name) > 20:
            return True
        else:
            return False

def not_valid_email(email):
    if len(email) <3 or len(email) >20:
        return True
    elif '@' not in email or '.' not in email:
        return True
    else:
        return False

        


app.run()

