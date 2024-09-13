import requests, json
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None) 

r= requests.get("https://randomuser.me/api/?results=5")
result = json.loads(r.content)


firstname = []
firstname.append(result['results'][0]["name"]["first"])
firstname.append(result['results'][1]["name"]["first"])
firstname.append(result['results'][2]["name"]["first"])
firstname.append(result['results'][3]["name"]["first"])
firstname.append(result['results'][4]["name"]["first"])

lastName = []
lastName.append(result['results'][0]["name"]["last"])
lastName.append(result['results'][1]["name"]["last"])
lastName.append(result['results'][2]["name"]["last"])
lastName.append(result['results'][3]["name"]["last"])
lastName.append(result['results'][4]["name"]["last"])


gender = []
gender.append(result["results"][0]["gender"])
gender.append(result["results"][1]["gender"])
gender.append(result["results"][2]["gender"])
gender.append(result["results"][3]["gender"])
gender.append(result["results"][4]["gender"])

emails = []
emails.append(result["results"][0]["email"])
emails.append(result["results"][1]["email"])
emails.append(result["results"][2]["email"])
emails.append(result["results"][3]["email"])
emails.append(result["results"][4]["email"])


person_df = pd.DataFrame(list(zip(firstname, lastName, gender, emails)), columns = ["First", "Last", "Gender", "Email"])
print(person_df)