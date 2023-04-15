import openai
import re
import os
import logging
import sys

def resource_path(relative_path):
  """ Get absolute path to resource, works for dev and for PyInstaller """
  try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "files/api-key.txt"
# abs_file_path = os.path.join(script_dir, rel_path)
abs_file_path = resource_path(rel_path)

with open(abs_file_path) as f:
  # authenticate openai
  api_key=f.readline()
  openai.api_key = api_key


#=======================================
# Trained Model Name: 
#=======================================

def generate_response(content):
  print("Waiting for GPT")

  #response = openai.ChatCompletion.create(
  #  model="gpt-3.5-turbo",
  #  messages=[
  #      {"role": "system", "content": ""},
  #      {"role": "user", "content": content}
  #    ]
  #)
  #return response['choices'][0]['message']['content']
  return "TESTTGSAASG"