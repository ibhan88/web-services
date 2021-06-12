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



################################################
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")


