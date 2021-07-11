from app import app
from flask import render_template
from pathlib import Path


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/blog.html")
def blog():
    return render_template("blog.html")

