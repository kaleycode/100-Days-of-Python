import os, json
from flask import Flask, request
import requests

# this program is simple: you press the button, you get a new joke :)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def change():
  page = ""
  f = open("jokes.html")
  page = f.read()
  f.close()
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  joke = result.json()
  page = page.replace("{jokes}", joke["joke"])
  return page

@app.route('/')
def index():
  page = ""
  f = open("jokes.html")
  page = f.read()
  f.close()
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  joke = result.json()
  page = page.replace("{jokes}", joke["joke"])
  return page

app.run(host='0.0.0.0', port=81)
