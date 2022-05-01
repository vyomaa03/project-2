from flask import Flask, render_template
import os

DATABASE_URL = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login')
def login(): # when the login button is pressed it should return this html
    return render_template('login.html')


@app.route('/signup')
def signup(): # when the login button is pressed it should return this html
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)