import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None) 

scraper = pd.read_html("https://en.wikipedia.org/wiki/List_of_best-selling_albums")

for index, table in enumerate(scraper):
    print(scraper[1])