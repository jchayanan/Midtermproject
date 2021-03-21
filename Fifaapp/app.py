from flask import Flask,render_template,request,redirect,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
from models import db,Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'
api_key = 'e204d64bf948417393062df65bdca4a3'
url = 'https://api.football-data.org/v2/{0}'

db.init_app(app)

headers = {
    'X-AUTH-TOKEN' : 'e204d64bf948417393062df65bdca4a3',
}

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    req = ''
    req = url.format("matches?status=LIVE")
    data = requests.get(req, headers={'X-AUTH-TOKEN':api_key}).json()
    return render_template('home.html', data=data)


@app.route("/standings")
def standings():
    req = ''
    req = url.format("competitions/2021/standings")
    data = requests.get(req, headers={'X-AUTH-TOKEN':api_key}).json()
    return render_template('standings.html', data=data)



@app.route("/competitions", methods = ['GET', 'POST'])
def competitions():
    if request.method == 'POST':
        league = request.form['league']
        league_url = "https://api.football-data.org/v2/competitions/{0}/scorers"
        req = ''
        req = league_url.format(league)
        data = requests.get(req, headers={'X-AUTH-TOKEN': api_key}).json()
        return render_template('competitions.html', data=data)
    else:
        req = ''
        req = url.format("competitions/WC/scorers")
        data = requests.get(req, headers={'X-AUTH-TOKEN': api_key}).json()
        return render_template('competitions.html', data=data)


@app.route("/teams", methods = ['GET', 'POST'])
def teams():
    if request.method == 'POST':
        teams = request.form['teams']
        teams_url = "https://api.football-data.org/v2/competitions/{0}/teams"
        req = ''
        req = teams_url.format(teams)
        data = requests.get(req, headers={'X-AUTH-TOKEN': api_key}).json()
        return render_template('teams.html', data=data)
    else:
        teams_url = "https://api.football-data.org/v2/competitions/{0}/teams"
        req = ''
        req = teams_url.format("CL")
        data = requests.get(req, headers={'X-AUTH-TOKEN': api_key}).json()
        return render_template('teams.html', data=data)


@app.route("/about")
def about():
    student = Student.query.all()
    return render_template('about.html', student=student)


if __name__ == "__main__":
   app.run(debug=True,port=8000)
   app.run()
