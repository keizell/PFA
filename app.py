from flask import Flask, render_template, request, redirect, session
from database import engine

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")


@app.route("/signup")
def signup():
  return render_template("Signup.html")


@app.route("/login")
def login():
  return render_template("Login.html")


@app.route('/main')
def main():
  return render_template("main.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


@app.route('/signup', methods=['POST'])
def put():
    # Get the data from the form
    username = request.form['username']
    email = request.form['email']
    name1 = request.form['name-1']
    name2 = request.form['name-2']
    password = request.form['password']
    telephone = request.form['telephone']
    # Insert the data into your MySQL database
    with engine.connect() as conn:
      sql = "INSERT INTO chercheur (username, email, password, fname, lname,   telephone) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (username, email, password, name1, name2, telephone)
      conn.execute(sql, val)
      db.commit()
    # Redirect the user back to the "chercheur" page
    return redirect('/main')