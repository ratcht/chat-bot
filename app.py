import json
import os
from flask import Flask, redirect, url_for, render_template, request
import sys

app = Flask(__name__)


@app.route("/home")
@app.route("/", methods=["GET"])
def index():
  return render_template("index.html")



@app.route("/chat", methods=["GET", "POST"])
def chat():
  if request.method == "GET":
    return render_template("chat-page.html")
  

  return render_template("chat-page.html")



if __name__ == "__main__":
  # webbrowser.open('http://127.0.0.1:8000')  # Go to example.com
  app.run(port=8000)


