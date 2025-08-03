from flask import Blueprint, render_template, request, redirect, session
import bcrypt

auth_blueprint = Blueprint('auth', __name__)

users = {
    "admin": bcrypt.hashpw("adminpass".encode('utf-8'), bcrypt.gensalt())
}

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode('utf-8')
        if username in users and bcrypt.checkpw(password, users[username]):
            session["user"] = username
            return redirect("/")
    return render_template("login.html")

@auth_blueprint.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")
