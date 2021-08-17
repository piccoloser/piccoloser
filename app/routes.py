from app import app
from app.forms import LoginForm
from flask import flash, redirect, render_template, url_for


@app.route("/")
def index():
    flash(
        "Oh hey, guess what... The site's actually being worked on!",
        category = "info"
    )
    flash(
        "This is a test of multiple messages.",
        category = "info"
    )
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("Logged in Successfully", category = "success")
        return redirect(url_for("blog"))
        

    else: flash(
        "Couldn't log in. Please make sure that you "
        "entered everything correctly. Only the site "
        "owner is permitted to post.",
        category = "failure"
    )

    return render_template("login.html", form = form)
