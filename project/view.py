from project import app
from flask import Flask , request , render_template , flash
from passlib.hash import sha256_crypt
import psycopg2

conn = psycopg2.connect(
    host=app.config["DB_SERVER"],
    port=app.config["DB_POST"],
    database=app.config["DB_NAME"],
    user=app.config["DB_USER"],
    password = app.config["DB_PASSWORD"])

user=[]

@app.route('/')
def index():
    global user
    if user == [] :
        return login() 
    try :
        cur = conn.cursor()
        s = "SELECT email,first_name,last_name,user_id FROM info_user"
        cur.execute(s)
        list_users = cur.fetchall()
        print(list_users)
        cur.close
        return render_template('index.html', list_users = list_users , user = user)
    except e :
        return render_template('index.html', list_users = list_users , user = user)


@app.route('/login')
def login():
    return render_template('login.html',title='Login') 


@app.route('/userLogin', methods=["POST"])
def userLogin():
    if request.method == 'POST':
        email=request.form["email"]
        password=request.form["password"]
        if not email :
            return render_template('login.html',title='Login') 
        if not password :
            return render_template('login.html',title='Login') 
        try :
            with conn: 
                cur = conn.cursor()
                query = "SELECT * FROM info_user WHERE email = '" + email + "' ;"
                cur.execute(query)
                global user
                user = cur.fetchall()
                cur.close
                if sha256_crypt.verify(password,user[0][4]):
                    return index()
                else :
                    return login() 
        except e :
            return login() 


@app.route('/register')
def register():
    return render_template('register.html',title='Register') 


@app.route('/getRegis', methods=["POST"])
def getRegis():
    if request.method == 'POST':
        
        fname=request.form["fname"]
        lname=request.form["lname"]
        email=request.form["email"]
        password=request.form["password"]
        passwordcon=request.form["passwordcon"]
        if not fname :
            return render_template('register.html',title='Register111')  
        if not lname :
            return render_template('register.html',title='Register111')  
        if not email :
            return render_template('register.html',title='Register111')  
        if password != passwordcon  :
            flash("The password don't match")
            return render_template('register.html',title='Register111') 
        password = sha256_crypt.encrypt(password) 
        try :
            with conn: 
                cur = conn.cursor()
                query = """INSERT INTO info_user(user_id, first_name, last_name, email ,pass)
                        VALUES(DEFAULT, %s ,%s ,%s , %s)"""
                values = ( fname, lname, email, password)
                cur.execute(query, values)
                conn.commit()
                cur.close()

                return register() 
        except e :
            return register() 
