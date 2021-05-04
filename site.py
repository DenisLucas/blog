from flask import Flask, render_template, request
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


@app.route('/projects', methods=["POST","GET"])
def projects():
    Apost = posts.query.filter_by(game=False)
    if request.method == "GET":
        if "id" in request.args: 
            post = posts.query.get(request.args.get("id"))
            return request.args.get("id")
            
    return render_template("projects.html", values=Apost)

@app.route('/games')
def games():
    return render_template("games.html")



@app.route('/admin', methods=["POST","GET"])
def Admin():
    if request.method == "POST":
        if "crud" in request.form:
            if request.form['crud'] == "create":
                create = True
                return render_template("admin.html", create=create)
            if request.form['crud'] == "update":
                update = True
                Pst = posts.query.all()
                return render_template("admin.html", values=Pst, update=update)
            if request.form['crud'] == "delete":
                delete = True
                Pst = posts.query.all()
                return render_template("admin.html", values=Pst, delete=delete)
        
        if "create" in request.form:
            title = request.form["title"]
            cont = request.form["content"]
            if "Game" in request.form:
                game = True
            else:
                game = False
            if "devlogs" in request.form:
                dev = True
            else:
                dev = False
            if "Tutorial" in request.form:
                tut = True
            else:
                tut = False

            post = posts(title,cont,game,tut,dev)
            dbCreate(post)
        
        
        if "delete" in request.form:
            post = posts.query.get(request.form["delete"])
            dbDelete(post)

        
        if "update" in request.form:
            post = posts.query.get(request.form["update"])
            return render_template("admin.html", values=post, upd=True)

        if "edit" in request.form:
            post = posts.query.get(request.form["edit"])
            
            title = request.form["title"]
            cont = request.form["content"]
            if "Game" in request.form:
                game = True
            else:
                game = False
            if "devlogs" in request.form:
                dev = True
            else:
                dev = False
            if "Tutorial" in request.form:
                tut = True
            else:
                tut = False
            edit = posts(title,cont,game,dev,tut)
            dbUpdate(edit,post)
    return render_template("admin.html")

def dbCreate(iten):
    db.session.add(iten)
    db.session.commit()

def dbDelete(iten):
    db.session.delete(iten)
    db.session.commit()

def dbUpdate(iten,post):
    dbCreate(iten)
    dbDelete(post)




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


