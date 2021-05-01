from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class posts(db.Model):
    _id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    post = db.Column(db.Text())
    
    game = db.Column(db.Boolean, default=False, nullable=False)
    tutorial = db.Column(db.Boolean, default=False, nullable=False)
    devlog = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self,title,post,game,tutorial,devlog):
        self.title = title
        self.post = post
        self.game = game
        self.tutorial = tutorial
        self.devlog = devlog


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/aboutme')
def aboutMe():
    return render_template("aboutme.html")


@app.route('/projects/devlogs')
def projectsD():
    return render_template("projectsD.html")

@app.route('/projects/tutorials')
def projectsT():
    return render_template("projectsT.html")


@app.route('/games/devlogs')
def gamesD():
    return render_template("gamesD.html")

@app.route('/games/tutorials')
def gamesT():
    return render_template("gamesT.html")

@app.route('/games/downloads')
def games():
    return render_template("games.html")


@app.route('/Admin')
def Admin():
    return render_template("Admin.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)