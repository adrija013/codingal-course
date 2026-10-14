from pathlib import Path

from flask import Flask, redirect, render_template_string, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "development-only-change-me"

# Demo-only account storage; accounts are cleared when the server restarts.
users = {}


def render_page(mode="login", message=""):
    template = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
    return render_template_string(template, mode=mode, message=message)


@app.get("/")
def home():
    return render_page()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_page()

    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")
    account = users.get(email)

    if account and check_password_hash(account["password"], password):
        session["email"] = email
        session["name"] = account["name"]
        return redirect(url_for("home"))

    return render_page(message="Incorrect email or password. Please try again.")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_page(mode="register")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not name or not email or not password:
        return render_page(mode="register", message="Please complete every field.")
    if email in users:
        return render_page(mode="register", message="An account with that email already exists.")

    users[email] = {"name": name, "password": generate_password_hash(password)}
    session["email"] = email
    session["name"] = name
    return redirect(url_for("home"))


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))