from flask import render_template, request, url_for
from app import app

name = "Unknown User"
@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    global name
    username = request.form.get("username")
    if username==None:
          user = {'username':name}
    else:
          user = {'username':username}
          name = username
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Sign In')