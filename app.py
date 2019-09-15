from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "fixed"

def get_username():
    if "username" in session: return session["username"]
    return False

@app.route("/")
def dashboard():
    username = get_username()
    if username:
        return render_template("dashboard.html", username=username)
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        return redirect(url_for("dashboard")) 

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("dashboard"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")

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
