from flask import Flask, redirect, request
from replit import db
import os

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.environ['secretKey']

db["user"] = {"username": "username", "password": "password"}

def getEntries():
  entry = ""
  with open("entry.html", "r") as f:
    entry = f.read()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content

@app.route('/')
def index():
  userid = request.headers['X-Replit-User-Id']
  print(userid)
  if userid == "111111":
    #replace "111111" with userid
    return redirect("/edit")
  elif userid:
    return redirect("/noAccess")
  page = ""
  f = open("blog.html", "r")
  page = f.read()
  page = page.replace("{content}", getEntries())
  return page

@app.route("/edit")
def edit():
  userid = request.headers['X-Replit-User-Id']
  if userid != "111111":
    #once again: replace "111111" with your userid
    return redirect("/")
  page = ""
  with open("edit.html", "r") as f:
    page = f.read()
  page = page.replace("{content}", getEntries())
  f.close()
  return page

@app.route("/add", methods=["POST"])
def add():
  userid = request.headers['X-Replit-User-Id']
  if userid != "111111":
    return redirect("/")
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "body": form["body"]}
  db[form["date"]] = entry
  return redirect("/edit")

@app.route("/noAccess")
def nope():
  return("🚫 No access for you! 🚫")

app.run(host='0.0.0.0', port=81)
