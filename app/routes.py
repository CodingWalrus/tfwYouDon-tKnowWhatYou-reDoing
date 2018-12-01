# Imports the render_template function from flask, also the flash and redirect functions
from flask import render_template
# Imports the app variable - defined in __init__.py from the app package
from app import app

@app.route('/')
@app.route('/index')
def index():
    #return 'Hello World!'
    return render_template('index.html', button_image = 'static/red_button.jpg', 
                            drake_clip = 'static/what_am_i_doing.mp3', favicon = 'static/icon.ico')