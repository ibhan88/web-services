import os
from flask import Flask, request, render_template, flash, redirect
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

@app.route('/contact-form', methods=['POST'])
def contact_form():
    """Handle contact form submission"""

    #UNFINISHED
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    companyname = request.form['companyname']
    email = request.form['email']
    description = request.form['description']

    flash('Your inquiry has been successfully submitted.')
    return redirect('/')



################################################
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")


