from flask import *

app = Flask(__name__)
app.secret_key = "fixed"
import sqlite3 as sql

@app.route('/')
def hello():
    return render_template("dashboard.html")

@app.route('/inventory')
def inventory():
    #return "Hello World!"
    return render_template("inventory.html")

"""
@app.route('/staff')
def staff():
    #return "Hello World!"
    return render_template("dashboard.html")

@app.route('/requests')
def requests():
    #return "Hello World!"
    return render_template("dashboard.html")

@app.route('/profile')
def profile():
    #return "Hello World!"
    return render_template("dashboard.html")

"""

if __name__ == '__main__':
    app.run(debug=True)