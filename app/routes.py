from app import app, bc, db, markdown
from app.forms import LoginForm, PostForm
from app.models import User, Post

from flask import flash, redirect, render_template, request, url_for

from flask_login import current_user, login_user, logout_user, login_required


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog")
def blog():
    posts = Post.query.all()

    return render_template("blog.html", markdown = markdown, posts = posts)


@app.route("/login", methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated: return redirect("blog")

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user and bc.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else redirect(url_for("blog"))

        else:    
            flash(
                "Couldn't log in. Please make sure that you entered everything "
                "correctly. Only the owner of this site is permitted to post.",
                category = "failure"
            )

    return render_template("login.html", form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/post/new", methods = ["GET", "POST"])
@login_required
def create_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            content = form.content.data,
            author = current_user
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("blog"))

    return render_template("create_post.html", form = form)


@app.route("/post/<int:post_id>")
def post(post_id: int):
    post = Post.query.get_or_404(post_id)

    return render_template("post.html", post = post)
