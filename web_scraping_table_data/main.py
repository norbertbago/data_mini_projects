from bs4 import BeautifulSoup
import pandas as pd
import csv

with open("index.htm") as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')


csvFile = open("cacao-rating.csv",'wt',newline='', encoding='utf-8')
writer = csv.writer(csvFile)

header = []
for element in soup.table.tr.find_all(class_=True):
    header.extend(element["class"])

writer.writerow(header)

rows = soup.find('tbody').find_all('tr')
for row in rows[1:-1]:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    writer.writerow(cols)
