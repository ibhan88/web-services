import os
from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from jinja2 import StrictUndefined
import json


app = Flask(__name__)
app.secret_key = "SECRET!"

db = SQLAlchemy()


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

@app.route('/portfolio/<int:project_id>')
def show_project(project_id):
    """Show detailed portfolio page for each project"""

    sql = "SELECT * FROM portfolio WHERE project_id = :project_id"

    cursor = db.session.execute(sql, {"project_id": project_id})
    project = cursor.fetchone()

    return render_template("project.html", project=project)

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
def connect_to_db(app):
    """Connect to database"""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///portfolio"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")


connect_to_db(app)  


