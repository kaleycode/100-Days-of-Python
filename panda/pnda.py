# Let's do some webscraping!!
# I am getting a table showing the most sold books ever from Wikipedia :D

from bs4 import BeautifulSoup
import requests
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None, "max_colwidth", 25) 

url = "https://en.wikipedia.org/wiki/List_of_best-selling_books"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find_all("tbody")[0]                #   first table from the website
table_headers = table.find_all("th")             #  gets table headers

table_headers_titles = [title.text.strip() for title in table_headers]

df = pd.DataFrame(columns=table_headers_titles)          #   setting our columns and making the dataframe
column_data = table.find_all("tr")[1:]                  #   getting rid of the empty [] at the top

for row in column_data:
    row_data = row.find_all("td")
    individual_row_data = [data.text.strip() for data in row_data]          #   getting our rows
    length = len(df)
    df.loc[length] = individual_row_data        #  now we have all the data from the first table from the website :) 
print(df)
