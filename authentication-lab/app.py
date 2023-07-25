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
  "measurementId": "G-47Z8DV47VK",
  "databaseURL":"https://atef-f7669-default-rtdb.firebaseio.com/"
    }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method=='POST':
        print('hi')
        email=request.form['email']
        password=request.form['password']
        try:
            print('hi')
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)   
            print('hi')
            return render_template("add_tweet.html")
        except:
            return render_template("signin.html")
    else:
        return render_template("signin.html")

    


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=""
    if request.method== 'POST':
        email=request.form['email']
        password = request.form['password']
        username = request.form['username']
        full_name = request.form['full_name']
        bio = request.form['bio']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user={"name":username,"email":email,"username":username, "full_name":full_name, 'bio': bio}
            UID = login_session['user']['localId']
            db.child("USers").child(UID).set(user)
            return render_template("add_tweet.html")
        except:
            print("errorrr")
            return render_template("signup.html")
    return render_template("signup.html") 



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method == 'POST':
        text = request.form['text']
        title = request.form['title']
        UID = login_session['user']['localId']
        tweet={"title":title, "text":text, "UID":UID}
        db.child("Tweets").push(tweet)
        return render_template("all_tweets.html")

    return render_template("add_tweet.html")




@app.route("/all_tweets", methods=['GET', 'POST'])
def all_tweets():
    tweets = db.child("Tweets").get().val()
    return render_template("all_tweets.html", tweets = tweets)






if __name__ == '__main__':
    app.run(debug=True)
