from flask import *
from database import init_db, db_session
from models import *
import random
import time

app = Flask(__name__)

app.secret_key = "sdfjowiefjw98r32jfhregu8392"

def populate():
    if len(db_session.query(Problem).all()) == 0:
        # skipping numbers in these variable titles is intentional
        p1_1 = Problem("Exponent equation", "Find the sum of all solutions x>0 to x^x = x^2.", "3", "algebra")
        p1_2 = Problem("Midpoints and diagonals", "Rectangle PQRS is placed in the coordinate plane. The midpoint of side PQ is at (3,4), and the midpoint of side QR is at (15, 9). What is the length of the diagonal of the rectangle?", "26", "geometry")
        p1_3 = Problem("A classic probability puzzle", "What is the probability that three random real numbers chosen uniformly between 0 and 1 have a sum less than 1? Enter your answer in the form \"a/b\" where gcd(a,b) = 1.", "1/6", "combinatorics")
        p1_4 = Problem("Primes?", "Suppose a prime p can be expressed as the sum of two primes. In how many other ways can p be expressed as the sum of two primes? Order does not matter. (Note: the answer is independent of p)", "0", "number theory")
        p2_2 = Problem("Distance between cylinder points", "In a right circular cylinder with radius 3 and height 4, find the square of the largest possible straight-line distance between two points on the cylinder.", "52", "geometry")
        p2_3 = Problem("Last digits base x", "What is the sum of the numbers x such that 13, 167, and 233 have the same last digit base x? (Assume x is not 1)", "35", "number theory")
        p2_4 = Problem("Mr. Redmond crosses a river", "Mr. Redmond and his class are trying to cross a river. Mr. Redmond has 10 students in his class. However, their boat can hold only 3 people at a time. What is the minimum number of trips that they need to take? (A trip is defined as going from one shore to the other.)", "9", "miscellaneous")
        p3_1 = Problem("An algebra puzzle", "Let a, b, c be real numbers. If (a+b)/c = 2 and (a+c)/b = 3, then what is (b+c)/a? Enter your answer in the form \"a/b\" where gcd(a,b) = 1.", "7/5", "algebra")
        p3_2 = Problem("Circle tangent to the hypotenuse", "Let ABC be a right triangle with angle C right. Let the smallest circle that passes through C and is tangent to AB be omega. Let omega intersect CA at P and CB at Q. If AC = 15 and BC = 20, what is PQ?", "12", "geometry")
        p3_4 = Problem("Limit", "Find the limit as n goes to infinity of (n!/n^n)^(1/n). Enter your answer in the form \"a/b.\"", "1/e", "calculus")
        p4_2 = Problem("A parallelogram classic", "In parallelogram ABCD, AB = 5, BC = 10, and AC = 13. What is the length of BD?", "9", "geometry")
        p4_3 = Problem("Josh Lowe numbers", "Call an integer n Josh Lowe if n does not divide (n-1)!. How many integers less than 100 are Josh Lowe?", "26", "number theory")
        p5_1 = Problem("Perpendicular distance", "Lines l_1 and l_2 are parallel with positive slope. If the perpendicular distance between them is 5 and the vertical distance between them is 13, then what is the slope of the lines? Enter your answer in the form \"a/b\" where gcd(a,b) = 1.", "12/13", "geometry")
        p5_2 = Problem("4-digit palindromes", "What is the probability that a 4-digit palindrome is even? Enter your answer in the form \"a/b\" where gcd(a,b) = 1.", "4/9", "combinatorics")
        p5_3 = Problem("Inversions", "Let a_i = 3i mod 100 for 1 <= i <= 99. For how many pairs (i, j) is i<j but a_i>a_j?", "1683", "number theory")
        p6_1 = Problem("Trigonometry", "Let f(x) = (x^2 - 2cos(1)x + 1)(x^2 - 2cos(2)x + 1) ... (x^2 - 2cos(179)x + 1), where all angles are measured in degrees. Find f(1).", "180", "algebra")
        p6_2 = Problem("Cevians", "Triangle ABC is right with angle B = 90. Point D is located on BC such that CD/BC = 1/2. Point E is located on AD such that CE bisects angle ACD. Let BC = 24. If the distance from point E to AB is 25/33 times the distance from point D to AB, then what is AC?", "25", "geometry")
        p6_3 = Problem("Conspirators", "Brutus, Cassius, and Caesar each put 8 dollars into an empty pot. Then a fair coin is flipped and each person bets whether it comes up heads or tails. However, Brutus and Cassius are conspiring and will always guess differently from each other. The pot is split equally among the people who guessed correctly. What is the expected value of Caesar's net gain (it may be negative)?", "-2", "combinatorics")
        p7_1 = Problem("Triangles and Hexagons", "Consider a regular triangle and a regular hexagon. Suppose that the sum of the area of the triangle and the perimeter of a hexagon equals the sum of the area of the hexagon and the perimeter of the triangle. Let the side length of the triangle be t, and the side length of the hexagon be s. There is an interval of t-values such that there exist no s that satisfy this condition. What is the length of this interval?", "4", "algebra")
        p7_2 = Problem("Factoring", "Find a if x=sqrt(a) satisfies 2x^4 + 15x^2 - 19x^2 - 285x - 361 = 0 and a is a positive integer.", "19", "algebra")
        p8_1 = Problem("Geometric probability with the circumcenter", "Consider a rectangle ABCD. Point P is selected uniformly at random on diagonal AC. Suppose that the probability that the circumcenter of CDP lies inside the rectangle is 1/3. What is the square of the ratio of the longer side of the rectangle to the shorter one?", "2", "geometry")
        p8_2 = Problem("Sum of numbers mod 3000", "What is the sum of the numbers from 1 to 2992 mod 3000?", "1528", "number theory")
        p9_2 = Problem("An infinite sequence of triangles", "Consider a right triangle ABC. Let P_0 be the midpoint of BC, and suppose that for each n, P_n is located halfway between P_(n-1) and B. Define Q_n as the point on AB directly above P_2. If tthe sum of the areas of the triangles ACP_0, Q_0P_0P_1, Q_1P_1P_2, Q_2P_2P_3, ... is 50, what is the sum of the areas of the triangles AP_0Q_0, Q_0P_1Q_1, Q_1P_2Q_1, ... ?", "25", "geometry")
        p9_3 = Problem("Perfect squares base b", "The 3-digit sequence 121 has the property that 121 base b is a perfect square for any base b>2, in which it is defined. How many 3-digit sequences whose digits are between 0 and 9 satisfy this property (the sequence cannot begin with a 0)?", "9", "number theory")
        p10_1 = Problem("Tricky trig equation", "Let the solution of sin(160-x)/sin(x) = 2sin(50) be x, where all angles are measured in degrees and 0<x<180. Find floor(x/7).", "4", "algebra")
        p10_2 = Problem("Approximation", "What is the integer closest to the solution to the equation x = cos(x), where x is in degrees?", "1", "geometry")
        p10_3 = Problem("Test placement", "Mr. Redmond gave his class a test, but now he has to rank people. In determining ties, Mr. Redmond takes the average of all the ranks of the people who tied if they were ordered randomly. For example, if three people score 100 (the highest score), then each of them receives 2nd place. In Mr. Redmond, there were ties for 1.5th place, 6th place, and 12th place. What is the minimum possible number of people in Mr. Redmond's class?", "15", "miscellaneous")
        p11_1 = Problem("Average grades", "Mr. Redmond was grading some tests. Before Student X's score was counted, the class average was 82.2. Mr. Redmond graded Student X's test last and found that Student X's score was 97. The new average was 82.6. How many students are in the class, including Student X?", "37", "algebra")
        p11_2 = Problem("Rolling dice", "I roll 5 distinguishable dice. What is the number of ways that the numbers can sum to 25? (Note: The numbers 5,5,4,6,5 would be counted as different than 6,4,5,5,5)", "5", "combinatorics")
        
        db_session.add_all([p1_1, p1_2, p1_3, p1_4, p2_2, p2_3, p2_4, p3_1, p3_2, p3_4, p4_2, p4_3, p5_1, p5_2, p5_3, p6_1, p6_2, p6_3, p7_1, p7_2, p8_1, p8_2, p9_2, p9_3, p10_1, p10_2, p10_3, p11_1, p11_2])
        db_session.commit()

@app.route("/")
def home():
    populate()
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
    populate()
    if "username" not in session:
        return redirect(url_for('login'))
    if request.method == "GET":
        problems_solved = db_session.query(User).where(User.username == session["username"]).first().problems_solved
        problems_unsolved = []
        for problem in db_session.query(Problem):
            if problem not in problems_solved:
                problems_unsolved.append(problem)
        if len(problems_unsolved)==0:
            return redirect(url_for('congrats'))
        rand_problem = random.choice(problems_unsolved)
        session["title"] = rand_problem.title
        session["starttime"] = time.time()
        return render_template("solve.html", problem=rand_problem, logged_in=True)
    if request.method=="POST":
        answer=request.form["answer"]
        current_problem = db_session.query(Problem).where(Problem.title==session["title"]).first()
        if current_problem.answer==answer:
            time_elapsed = round(time.time() - session["starttime"])
            flash("Nice job! That took you " + str(time_elapsed) + " seconds", "info")
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

@app.route("/reset")
def reset():
    if "username" not in session:
        return redirect(url_for('login'))
    else:
        db_session.query(User).where(User.username == session["username"]).first().problems_solved = []
        db_session.commit()
        flash("Your progress has been cleared", "info")
        return redirect(url_for('solve'))

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
