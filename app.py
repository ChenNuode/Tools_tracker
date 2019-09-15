from flask import Flask, render_template, session, redirect, url_for, request
from base import Base, engine, Session
from classes import User, Item, Request
from hash import hash

app = Flask(__name__)
app.secret_key = "fixed"

Base.metadata.create_all(engine)
db_session = Session()

def get_name():
    if "name" in session: return session["name"]
    return False

@app.route("/")
def dashboard():
    name = get_name()
    if name:
        return render_template("dashboard.html", name=name)
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        name = request.form["name"]
        password = request.form["password"]
        user = db_session.query(User).filter_by(name=name).first()
        if user is None or user.password != hash(password):
            return render_template("login.html", error="Invalid Username or Password")
        session["name"] = name
        return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect(url_for("dashboard"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        type_no = int(request.form["type_no"])
        location = request.form["location"]
        name = request.form["name"]
        password = request.form["password"]
        if not (1 <= type_no and type_no <= 3):
            return render_template("signup.html", error="Invalid Type")
        if location is "":
            return render_template("signup.html", error="No Location Specified")
        if name is "":
            return render_template("signup.html", error="No Name Specified")
        if password is "":
            return render_template("signup.html", error="No Password Specified")
        password = hash(password)
        user = User(type_no, location, name, password)
        db_session.add(user)
        db_session.commit()
        return redirect(url_for("login"))


@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/staff")
def staff():
    return render_template("dashboard.html")

@app.route("/requests")
def requests():
    return render_template("dashboard.html")

@app.route("/profile")
def profile():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
