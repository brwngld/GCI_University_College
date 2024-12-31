from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('root/index.html')

@app.route('/courses')
def courses():
    return render_template('root/course-listing.html')

@app.route('/strategic_plan')
def strategic_plan():
    return render_template('root/about.html')

@app.route('/user_register')
def user_register():
    return render_template('root/register.html')

@app.route('/contact')
def contact():
    return render_template('root/contact.html')


@app.route('/gallery')
def gallery():
    return render_template('root/gallery2.html')
