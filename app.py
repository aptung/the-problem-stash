from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

app.secret_key = "sdfjowiefjw98r32jfhregu8392"

# TODO: Fill in methods and routes

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
