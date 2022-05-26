"""
web server using flask and jinja templating
index.html should be under "templates" folder
other resources should be under "static" folder
"""
import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, copyright_year=year)



if __name__ == "__main__":
    app.run()