from project import app

from flask import Flask , request , render_template
import psycopg2

conn = psycopg2.connect(
    host=app.config["DB_SERVER"],
    port=app.config["DB_POST"],
    database=app.config["DB_NAME"],
    user=app.config["DB_USER"],
    password = app.config["DB_PASSWORD"])

@app.route('/')
def index():
    cur = conn.cursor()
    s = "SELECT email,first_name,last_name,user_id FROM info_user"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)


@app.route('/login')
def login():
    return render_template('login.html') 


@app.route('/register')
def register():
    return render_template('register.html') 


@app.route('/getRegis')
def getRegis():
    return render_template('login.html') 