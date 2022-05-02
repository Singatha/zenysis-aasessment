from flask import Flask
import requests
import json

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Case, Vaccine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://covid_info_user:covid1234@localhost/covid_info"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
migrate = Migrate(app, db)

base_api_url = "https://covid-api.mmediagroup.fr/v1"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cases")
def get_cases():
    request = requests.get("https://covid-api.mmediagroup.fr/v1/cases?country=France")
    data = request.json()
    data = data["All"]
    case = Case(data["confirmed"], data["recovered"], data["deaths"], data["country"])
    
    db.session.add(case)
    db.session.commit()

    return data

@app.route("/vaccines")
def get_vaccines():
    request = requests.get("https://covid-api.mmediagroup.fr/v1/vaccines?country=France")
    data = request.json()
    data = data["All"]
    vaccine = Vaccine(data["administered"], data["people_vaccinated"], data["people_partially_vaccinated"], data["country"])
    
    db.session.add(vaccine)
    db.session.commit()

    return data


if __name__ == '__main__':
   app.run()
