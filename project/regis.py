from flask import Flask 
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField


class regis(FlaskFrom) :
    email = TextField('')
    password = TextField('')
    first_name = TextField('')
    last_name = TextField('')
    submit = SubmitField('')