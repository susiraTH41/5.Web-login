from project import app
from flask import Flask , request , render_template

import psycopg2

conn = psycopg2.connect(
    host=app.config["DB_SERVER"],
    port=app.config["DB_POST"],
    database=app.config["DB_NAME"],
    user=app.config["DB_USER"],
    password = app.config["DB_PASSWORD"])

user = ["susira","tulapongsa"]

@app.route('/')
def index():
    if user == [] :
        return login() 
    
    cur = conn.cursor()
    s = "SELECT email,first_name,last_name,user_id FROM info_user"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users , user = user)


@app.route('/login')
def login():
    user = []
    return render_template('login.html',title='Login') 


@app.route('/register')
def register():
    return render_template('register.html',title='Register') 


@app.route('/getRegis', methods=["POST"])
def getRegis():
    cursor = conn.cursor()
    fname=request.form.get("fname")
    lname=request.form.get("lname")
    email=request.form.get("email")
    password=request.form.get("password")
    passwordcon=request.form.get("passwordcon")
    if password != passwordcon :
        return render_template('register.html',title='Register111')  
    query = """INSERT INTO info_user(user_id, first_name, last_name, email ,pass)
            VALUES(DEFAULT, %s ,%s ,%s , %s)"""
    values = ( fname, lname, email, password)
    cursor.execute(query, values)
    cursor.close()


 
    return register() 


