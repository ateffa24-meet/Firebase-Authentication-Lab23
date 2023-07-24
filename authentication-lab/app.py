from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyBRazhO5MEcR66YfOSwIZ5oJ-4Eo2Op3tU",
  "authDomain": "atef-f7669.firebaseapp.com",
  "projectId": "atef-f7669",
  "storageBucket": "atef-f7669.appspot.com",
  "messagingSenderId": "570090090631",
  "appId": "1:570090090631:web:e519920dab366562074822",
  "measurementId": "G-47Z8DV47VK"
    }

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.methods=='post':
        email=request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.creat_user_with_email_and_password(email, password)
        except:
            return render_template("signin.html")

    


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=""
    if request.methods== 'POST':
        email=request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.creat_user_with_email_and_password(email, password)
        except:
            return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)
