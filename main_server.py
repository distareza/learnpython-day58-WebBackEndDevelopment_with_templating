"""
web server using flask and jinja templating
index.html should be under "templates" folder
other resources should be under "static" folder
"""
import datetime
import random

import requests as requests
from flask import Flask, render_template
import markupsafe
import json

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, copyright_year=year)


@app.route('/guess/<name>')
def get_guess(name):
    def predict_age(name):
        try:
            response = requests.get(f"https://api.agify.io/?name={markupsafe.escape(name)}")
            data = json.loads(response.text)
            return data['age']
        except:
            return "unknown"

    def predict_gender(name):
        try:
            response = requests.get(f"https://api.genderize.io/?name={markupsafe.escape(name)}")
            data = json.loads(response.text)
            return data['gender']
        except:
            return "unknown"

    age = predict_age(name)
    gender = predict_gender(name)
    return  render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/5c46f4b733065c7f3f6d"
    response = requests.get(blog_url)
    post_json = response.json()
    return render_template("blog.html", posts=post_json)

if __name__ == "__main__":
    app.run()