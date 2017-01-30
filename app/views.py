from app import app
from flask import render_template, flash, redirect, Response, request, Flask
from .forms import LoginForm
from functools import wraps

def check_auth(username,password):
    return username == "Hijtec" and password == "alice"

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
    
@app.route("/news")
def news():
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
    
@app.route("/editor")
def editor():
    return render_template("editor.html",
                           title="My blog")

@app.route("/unlimitedmemory")
def unlimitedmemory():
    return render_template("articles/unlimitedmemory.html",
                           topics=["How to learn stuff", "Koncentrace", "Základy", "Techniky"]
                           title="Unlimited Memory")
    