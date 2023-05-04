from flask import *
from database import init_db, db_session
from models import *
import random

app = Flask(__name__)

app.secret_key = "sdfjowiefjw98r32jfhregu8392"


@app.route("/")
def home():
    # testproblem=Problem("Test problem", "here is some content for the test problem", "42", "algebra")
    # testproblem2=Problem("Test problem2", "new content", "21", "geometry")
    # testproblem3=Problem("Test problem3", "sdssdfsdsd", "1", "algebra")
    # testproblem4=Problem("Test problem4", "sdssdsdsdfsdffsdsd", "3", "number theory")
    # testproblem5=Problem("Test problem5", "sdssdefeefeffeefeffsdsd", "7", "algebra")
    # testproblem6=Problem("Test problem6", "sdfwefijwgerwwee", "17", "algebra")
    # testuser=User("test1", "password1")
    
    # db_session.add(testproblem)
    # db_session.add(testproblem2)
    # db_session.add(testproblem3)
    # db_session.add(testproblem4)
    # db_session.add(testproblem5)
    # db_session.add(testproblem6)
    # db_session.add(testuser)
    # db_session.commit()

    
    problems = random.sample(list(db_session.query(Problem)), 6)
    logged_in = "username" in session
    return render_template("home.html", problem1 = problems[0], problem2 = problems[1], problem3 = problems[2], problem4 = problems[3], problem5 = problems[4], problem6 = problems[5], logged_in=logged_in)

@app.route("/login", methods=("GET", "POST"))
def login():
    if "username" in session:
        return redirect(url_for('solve'))
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
        return redirect(url_for('solve'))

@app.route("/signup", methods=("GET", "POST"))
def signup():
    if "username" in session:
        return redirect(url_for('solve'))
    if request.method=="GET":
        return render_template("signup.html")
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        user = db_session.query(User).where(User.username==username).first()
        if user is not None:
            flash("That username is already taken", "error")
            return render_template("signup.html", logged_in=False)
        elif password != password2:
            flash("Those passwords don't match", "error")
            return render_template("signup.html", logged_in=False)
        else:
            new_user=User(username, password)
            db_session.add(new_user)
            db_session.commit()
            flash("Your account has been created and you have been logged in!", "info")
        session["username"] = username
        return redirect(url_for('solve'))
    

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
    if "username" not in session:
        return redirect(url_for('login'))
    if request.method == "GET":
        problems_solved = db_session.query(User).where(User.username == session["username"]).first().problems_solved
        problems_unsolved = []
        for problem in db_session.query(Problem):
            if problem not in problems_solved:
                problems_unsolved.append(problem)
        if len(problems_unsolved)==0:
            # flash("You solved all the problems! Congrats!", "info")
            return redirect(url_for('congrats'))
        rand_problem = random.choice(problems_unsolved)
        session["title"] = rand_problem.title
        return render_template("solve.html", problem=rand_problem, logged_in=True)
    if request.method=="POST":
        answer=request.form["answer"]
        current_problem = db_session.query(Problem).where(Problem.title==session["title"]).first()
        if current_problem.answer==answer:
            flash("Nice job!", "info")
            current_user = db_session.query(User).where(User.username == session["username"]).first()
            current_user.problems_solved.append(current_problem)
            db_session.commit()
            return redirect(url_for('solve'))
        else:
            flash("That's incorrect", "info")
            return render_template("solve.html", problem=current_problem, logged_in=True)

# this assumes we are already logged in
@app.route("/recentlysolved")
def recentlysolved():
    if "username" not in session:
        return redirect(url_for('login'))
    # .all() ensures that a list is returned instead of an iterator
    problems_dates = db_session.query(Problem, Solve.time_solved).where(Problem.title==Solve.problem_id).join(Solve, Solve.user_id==session["username"]).group_by(Problem.title).order_by(desc(Solve.time_solved)).limit(10).all()
    return render_template("recentlysolved.html", problems_dates = problems_dates, logged_in=True)

@app.route("/congrats")
def congrats():
    return render_template("congrats.html", logged_in=True)

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
