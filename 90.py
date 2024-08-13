#day 90 of 100 days of code:
import requests, json, time

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
    user = result.json()
    for person in user["results"]:
      filename = f"""{person["name"]["first"].lower()}_{person["name"]["last"].lower()}.jpg"""
      picture = requests.get(person["picture"]["medium"])
      f = open(filename, "wb")
      f.write(picture.content)
      f.close()
      print(f"{filename}")
      time.sleep(0.3)