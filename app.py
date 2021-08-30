from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
from models import db, connect_db, User, Bet


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///crappysports_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'coolbeans'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():

    url = "https://odds.p.rapidapi.com/v1/odds"

    querystring = {"sport": "americanfootball_nfl", "region": "us",
                   "mkt": "h2h", "dateFormat": "iso", "oddsFormat": "decimal"}

    headers = {
        'x-rapidapi-host': "odds.p.rapidapi.com",
        'x-rapidapi-key': "462e5708d7msh6be12143d24c056p1a05b0jsn6f202208f183"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)

    return render_template("home_page.html", response=response.text[1])


@app.route("/accounts")
def accounts():
    return render_template("account_page.html")


@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["password"]

    new_user = User(username=username, password=password)
    return redirect("/")
