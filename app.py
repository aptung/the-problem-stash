from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

app.secret_key = "sdfjowiefjw98r32jfhregu8392"

# TODO: Fill in methods and routes

@app.route("/")
@app.route("/home")
def home():
    # testproblem=Problem("Test problem", "here is some content for the test problem", "42", "algebra")
    # testuser=User("test1", "password1")
    
    # db_session.add(testproblem)
    # db_session.add(testuser)
    # db_session.commit()
    # testproblem.solved_by.append(testuser)
    # db_session.commit()

    return render_template("home.html")

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        user = db_session.query(User).where(User.username==username).first()
        if user is None:
            flash("That username does not exist", "error")
            return render_template("login.html")
        if user.password != password:
            flash("Your password is incorrect", "error")
            return render_template("login.html")
        session["username"] = username
        return redirect(url_for('home'))

@app.route("/solve")
def solve():
    return render_template("solve.html")

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
