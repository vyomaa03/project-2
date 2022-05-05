from unittest import result
from flask import Flask, redirect, render_template, request
import os
import weather
import json
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

@app.route('/weather')
def not_main():
    return render_template('user_main.html')

@app.route('/weather_get', methods=['post'])
def main():
    lat = request.form.get('lat')
    lon = request.form.get('lon')
    result = weather.weather_get(lat,lon)
    print(result)
    return redirect('/weather')


if __name__ == '__main__':
    app.run(debug=True)