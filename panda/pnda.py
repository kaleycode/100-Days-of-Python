from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_best-selling_books"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("table")[0]
tr = table.find_all("tr")

book_titles = [title.text for title in tr]

column_data = table.find_all("tr")
for row in column_data[1:]:
    row.find_all("td")
    list_row_data = [data.text.strip() for data in row.find_all("td")]
    list_row_data = [data.replace(">", "") for data in list_row_data]
    print(list_row_data)