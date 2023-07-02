from flask import Flask, render_template, request, redirect, session
from database import engine

app = Flask(__name__)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)


@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/index")
def hello_world():
  return render_template("index.html")
  
@app.route("/login")
def login():
  return render_template("login.html")

@app.route('/home')
def main():
  return render_template("home.html")


