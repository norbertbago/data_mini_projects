import requests as re
import json
import pandas as pd
from  bs4 import BeautifulSoup
 
df    = re.get("https://calendar.zoznam.sk/sunset-sk.php?city=3058531")
soup  = BeautifulSoup(df.text, 'html.parser')

mydivs = soup.findAll("div", {"class": "calendar"})

year = {}
number_of_month = 0

for div in mydivs:

    days_in_month = 0
    number_of_month += 1
    months = {}
    
    month = div.h2.text
    tds = div.find_all("span", {"class": "number"})
    days = {}
    
    for td in tds:
       day = td.parent.text
       days_in_month +=1
    #    sun_set = day.rsplit('Západ:')
    #    sun_rise = day.split('Vychod:')
       days[days_in_month] = day
    

    months["number of month"] = number_of_month
    months["days in month"] = days_in_month
    months["days data"] = days
    year[month] = months



with open('output.json', 'w') as json_file:
  json.dump(year, json_file)

