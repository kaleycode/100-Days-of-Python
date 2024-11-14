#day 90 of 100 days of code:
import requests, json, time

for i in range(15):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
    for person in user["results"]:
      filename = f"""{person["name"]["first"].lower()} {person["name"]["last"].lower()}\nemail: {person["email"].lower()}\n\n"""
      f = open(filename, "wb")
      f.close()
      print(f"{filename}")
      time.sleep(0.2)
######
