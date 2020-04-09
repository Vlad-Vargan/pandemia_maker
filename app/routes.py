from flask import render_template
from app import app
from .database import DB

@app.route('/')
@app.route('/index')
def index():

    parts_0 = DB.get_parts(1)
    parts_1 = DB.get_parts(2)
    parts_2 = DB.get_parts(3)
    parts_3 = DB.get_parts(4)
    
    BOX = [
        ["tab11", parts_0],
        ["tab12", parts_1],
        ["tab13", parts_2],
        ["tab14", parts_3]
        ]
        

    return render_template('index.html', BOX = BOX)