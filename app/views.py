from app import app
from flask import render_template, flash, redirect, Response, request, Flask
from .forms import LoginForm
from functools import wraps

def check_auth(username,password):
    return username == "admin" and password == "alice"

def authenticate():
    return Response('Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/")
@app.route("/index")
def index():
    posts=[{"author":"Hijtec", "body":"A first post"}]
    return render_template("index.html",
                           title="My blog",
                           posts=posts,
                           activenav1="active")

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    admin = {"adminname":"Hijtec", "password":"alice"}
    form = LoginForm()
    return render_template("admin_login.html",
                           form=form,
                           admin=admin,
                           title="Administration",)
    
@app.route("/news")
def about():
    title="Version 1"
    return render_template("news.html",
                           title=title,
                           activenav1="active")
    
@app.route("/about")
def about():
    return render_template("about.html",
                           title="My blog",
                           activenav2="active")
    
@app.route("/contacts")
def contacts():
    information=[{"owner":"Hijtec", 
                  "name":"Martin", "lastname":"Černil", 
                  "telephone":"number", "email":"emailadress",
                  }]
    return render_template("contacts.html",
                           information=information,
                           title="My blog",
                           activenav3="active")
    
@app.route("/administration")
@requires_auth
def administration():
    return render_template("/administration.html",
                           title="Administration")
    