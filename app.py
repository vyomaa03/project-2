from ast import Return
from crypt import methods
import email
from unittest import result
from flask import Flask, g, redirect, render_template, request, session
import os
import weather
import json
import psycopg2
import bcrypt
from database import sql_fetch, sql_write

DATABASE_URL = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY', 'something')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def get_user_name():
  if 'user_id' in session:
    user_id = session['user_id']
    results = sql_fetch('SELECT name FROM users WHERE id = %s', [user_id])
    name = results[0][0]
    return name
  return ''


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_action():
    email = request.form.get('username')
    password = request.form.get('password') 
    rows = sql_fetch('SELECT id, name, password_hash FROM users WHERE email = %s', [email])
    if len(rows) != 0:
        user_id = rows[0][0]
        name = rows[0][1]
        password_hash = rows[0][2]
        print(name, password_hash)
        valid = bcrypt.checkpw(password.encode(), password_hash.encode())
        print(valid)
        session['user_id'] = user_id
        return redirect('/weather')
    else:
        print('invalid email')
        return redirect('/login')


@app.route('/add_location', methods=['POST'])
def addLocation():
    latitude = request.form.get('lat')
    longitude = request.form.get('lon')
    sql_write("INSERT INTO locations (latitude, longitude) VALUES (%s, %s)", [latitude, longitude])
    print('done')
    return redirect('/weather')


@app.route('/signup')
def signup(): 
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_action():
  email = request.form.get('username')
  password = request.form.get('password')
  pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
  sql_write("INSERT INTO users (email, name, password_hash) VALUES (%s, %s, %s)", [email, 'name', pw_hash])
  print('done')
  return redirect('/weather')

@app.route('/weather')
def not_main():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    rows = sql_fetch('SELECT latitude FROM locations')
    rows2 = sql_fetch('SELECT longitude FROM locations')
    if latitude == None:
        return render_template('user_main.html', rows=rows, rows2=rows2)
    else:
        latitude = request.args.get('lat')
        longitude = request.args.get('lon')
        rows = sql_fetch('SELECT latitude FROM locations WHERE latitude = %d', [latitude])
        rows2 = sql_fetch('SELECT longitude FROM locations WHERE longitude = %d', [longitude])
        print(rows)
        result = weather.weather_get(latitude,longitude)
        print(result)
        timezone = result['timezone']
        humidity = result['current']['humidity']
        pressure = result['current']['pressure']
        clouds = result['current']['clouds']
        visibility = result['current']['visibility']
        speed = result['current']['wind_speed']
        gust = result['current']['wind_gust']
        heading = result['current']['wind_deg']
        return render_template('user_main.html', rows=rows, rows2=rows2, timezone=timezone,humidity=humidity, pressure=pressure, clouds=clouds, visibility=visibility,speed=speed, gust=gust, heading=heading)
    

if __name__ == '__main__':
    app.run(debug=True)