import json
import os
from flask import Flask, redirect, url_for, render_template, request
from files.chatObject import ChatObject
from files.gptAPI import generate_response
import time
import sys

app = Flask(__name__)

session_chat = []


@app.route("/home")
@app.route("/", methods=["GET"])
def index():
  return render_template("index.html")

@app.route("/chat-list", methods=["GET"])
def chat_list():

  return render_template("partials/chat-partial.html", loaded_chat=session_chat)

@app.route("/chat", methods=["GET", "POST"])
def chat():

  if request.method == "GET":
    return render_template("chat-page.html", loaded_chat=[])
  
  chat_input = request.get_json()

  # Send Chat to GPT
  chat_response = generate_response(chat_input)
  chat = ChatObject(chat_input, chat_response)
  session_chat.append(chat)

  return json.dumps(chat_input)

# Load from file
@app.route("/load", methods=["POST"])
def load_from_file():
  if request.method == "GET":
    return redirect(url_for('not_found'))
  
  # Load from file
  print(request.get_data())
  chat_array = []

  return redirect(url_for("chat-page.html", loaded_chat=chat_array))

@app.route("/404", methods=["GET", "POST"])
def not_found():
  return render_template("404.html")

if __name__ == "__main__":
  # webbrowser.open('http://127.0.0.1:8000')  # Go to example.com
  app.run(port=8000)


