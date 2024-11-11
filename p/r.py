import requests
from bs4 import BeautifulSoup

link =  "https://coppermind.net/wiki/Renarin_Kholin"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('div', class_='mw-parser-output'))
#print(soup.find_all('div', class_='mw-parser-output')[0].get_text())
#print(soup.find_all('div', class_='mw-parser-output')[0].find_all('p'))
#print(soup.find_all('div', class_='mw-parser-output')[0].find_all('p')[0].get_text())
#print(soup.find_all('div', class_='mw-parser-output')[0].find_all('p')[0].find_all('a'))
