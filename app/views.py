from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    posts=[{"author":"Hijtec", "body":"A first post"}]
    return render_template("index.html",
                           title="My blog",
                           posts=posts,
                           activenav1="active")
@app.route("/admin_login")

def admin_login():
    admin=[{"adminname":"Hijtec", "password":"Alice"}]
    return render_template("admin_login.html",
                           admin=admin,
                           title="Administration")
    
@app.route("/about")
def about():
    information=[{"owner":"Hijtec", 
                  "name":"Martin", "lastname":"Černil", 
                  "telephone":"number", "email":"emailadress",
                  }]
    return render_template("about.html",
                           information=information)
    
@app.route("/contacts")
def contacts():
    information=[{"owner":"Hijtec", 
                  "name":"Martin", "lastname":"Černil", 
                  "telephone":"number", "email":"emailadress",
                  }]
    return render_template("contacts.html",
                           information=information)