from flask import *
from database import init_db, db_session
from models import *
import random

app = Flask(__name__)

app.secret_key = "sdfjowiefjw98r32jfhregu8392"

# TODO: Fill in methods and routes

@app.route("/")
def home():
    # testproblem=Problem("Test problem", "here is some content for the test problem", "42", "algebra")
    # testuser=User("test1", "password1")
    
    # db_session.add(testproblem)
    # db_session.add(testuser)
    # db_session.commit()
    # testproblem.solved_by.append(testuser)
    # db_session.commit()
    
    # testproblem2=Problem("Test problem2", "new content", "21", "geometry")
    # db_session.add(testproblem2)
    # db_session.commit()

    logged_in = "username" in session
    return render_template("home.html", logged_in=logged_in)

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

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("You've been logged out", "info")
    else:
        flash("You're not logged in", "info")
    return redirect(url_for("login"))

@app.route("/solve", methods=("GET", "POST"))
def solve():
    logged_in = "username" in session
    if request.method == "GET":
        problems_solved = db_session.query(User).where(User.username == session["username"]).first().problems_solved
        problems_unsolved = []
        for problem in db_session.query(Problem):
            if problem not in problems_solved:
                problems_unsolved.append(problem)
        if len(problems_unsolved)==0:
            flash("You solved all the problems! Congrats!", "info")
            return redirect(url_for('home'))
        rand_problem = random.choice(problems_unsolved)
        session["title"] = rand_problem.title
        return render_template("solve.html", problem=rand_problem, logged_in=logged_in)
    if request.method=="POST":
        answer=request.form["answer"]
        current_problem = db_session.query(Problem).where(Problem.title==session["title"]).first()
        if current_problem.answer==answer:
            flash("Nice job!", "info")
            current_user = db_session.query(User).where(User.username == session["username"]).first()
            current_user.problems_solved.append(current_problem)
            db_session.commit()
            return redirect(url_for('solve'), logged_in=logged_in)
        else:
            flash("That's incorrect", "info")
            return render_template("solve.html", problem=current_problem, logged_in=logged_in)
            
    


@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
