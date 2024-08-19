import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/A._J._Raffles_(character)"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

text = ""

article = soup.find_all("div", {"class": "mw-heading mw-heading3"})

for i in article:
  text += i.text
  print(i.text.replace("[edit]", ""))
