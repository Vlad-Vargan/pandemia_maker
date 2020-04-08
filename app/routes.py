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
    
    return render_template('index.html', parts_0 = parts_0, 
                                            parts_1 = parts_1, 
                                            parts_2 = parts_2,
                                            parts_3 = parts_3)