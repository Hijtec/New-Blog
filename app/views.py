from app import app
from flask import render_template, flash, redirect, Response, request, Flask
from .forms import ContactForm
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
                           maintitle="My blog",
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
    
@app.route("/contacts", methods = ['GET', 'POST'])
def contacts():
    information=[{"owner":"Hijtec", 
                  "name":"Martin", "lastname":"Černil", 
                  "telephone":"number", "email":"emailadress",
                  }];
    
@app.route("/administration")
@requires_auth
def administration():
    return render_template("/administration.html",
                           title="Administration")

@app.route("/unlimitedmemory")
def unlimitedmemory():
    return render_template("articles/unlimitedmemory.html",
                           topics=["How to learn stuff", "Koncentrace", "Základy", "Techniky"],
                           title="Unlimited Memory",
                           headings=['1. Koncentrace', '2. Základy', '3. Techniky', '4. Čísla', '5. Mind mapping', '6. Metody života', '7. Sebedisciplína', 'Pro oživení opakujte!', '9. Souhrn'],
                           conclusions=["Mindmap of Unlimited Memory"])

@app.route("/artofbanter")
def artofbanter():
    return render_template("articles/artofbanter.html",
                           topics=["How to learn stuff", "Banter", "Základy", "Techniky", "Komunikace"],
                           title="Art of Banter")
    
@app.route("/advancedprocrastinationhacks")
def advancedprocrastinationhacks():
    return render_template("articles/APH.html",
                           topics=["How to learn stuff", "Procrastination", "Základy", "Techniky", "Productivity"],
                           headings=['Proč inteligentí lidé prokrastinují', 'Návyk Následující Akce', 'Setrvačnost: Fyzika a Produktivita', 'To-Do List: znovu a lépe', 'Dvouminutové Pravidlo', 'Velké Cíle a Malé Kvóty', 'Časové Bloky', 'Metoda Zadek v Křesle', 'Vytvořte si "To-Do List" Rozptylování', 'Metoda (10+2)*5', 'Využijte uzávěrek', 'Zastřelte svého vnitřního Perfekcionistu', 'Jak produktivně prokrastinovat', 'Vizualizace, která vede k prokrastinaci (a která ne)', 'Slovo, které zabíjí prokrastinaci', 'Jak hravě a rychle používat Outsourcing', 'Shrnutí a Závěr'],
                           title="Advanced Procrastination Hacks",
                           conclusions=["Mindmap of APH"])

@app.route("/doporucene_veci")
def advancedprocrastinationhacks():
    return render_template("articles/doporucene_veci.html",
                           title="Doporučené věci")
    