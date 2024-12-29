from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('root/index.html')

@app.route('/courses')
def courses():
    return render_template('root/courses.html')