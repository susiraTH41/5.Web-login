from flask import Flask 

app = Flask(__name__, static_folder='templates/assert' )
app.config.from_object('config.DevelopmentConfig')

    
from project import view 