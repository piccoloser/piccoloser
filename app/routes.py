from app import app, bc, db, markdown
from app.forms import LoginForm, PostForm
from app.models import User, Post

from flask import abort, flash, redirect, render_template, request, url_for

from flask_login import current_user, login_user, logout_user, login_required


@app.route("/")
def home():
    return render_template("home.html", title = "_piccoloser")


@app.route("/about")
def about():
    return render_template("about.html", title = "about")


@app.route("/blog")
def blog():
    posts = Post.query.all()

    return render_template(
        "blog.html",
        title = "blog",
        markdown = markdown,
        posts = posts
    )


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

    return render_template("login.html", title = "login", form = form)

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
            author = current_user,
            draft = form.draft.data,
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("blog"))

    return render_template(
        "post_actions.html", 
        title = "create post", 
        form = form,
        legend = "create post",
    )


@app.route("/post/<int:post_id>/delete", methods = ["GET", "POST"])


@app.route("/post/<int:post_id>/edit", methods = ["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if post.author != current_user: abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.draft = form.draft.data

        db.session.commit()
        
        flash("Your post has been updated!", category = "success")
        return redirect(url_for("post", post_id = post_id))
    
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
        form.draft.data = post.draft

    return render_template(
        "post_actions.html", 
        title="edit post", 
        form = form,
        legend = "edit post",
    )


@app.route("/post/<int:post_id>")
def post(post_id: int):
    post = Post.query.get_or_404(post_id)

    return render_template("post.html", title = post.title, post = post)
