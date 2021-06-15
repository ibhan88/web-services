import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import StrictUndefined
import json


app = Flask(__name__)
app.secret_key = "SECRET!"


@app.route('/')
def index():
    """Show homepage"""

    return render_template("index.html")

@app.route('/about')
def about():
    """Show informative About page"""

    return render_template("about.html")

@app.route('/services')
def services():
    """Show page that lists and describes services offered"""

    return render_template("services.html")

@app.route('/pricing')
def pricing():
    """Show pricing tiers page"""

    return render_template("pricing.html")

@app.route('/portfolio')
def portfolio():
    """Show portfolio index"""

    return render_template("portfolio.html")

@app.route('/contact')
def contact():
    """Show contact page"""

    return render_template("contact.html")



################################################
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")


