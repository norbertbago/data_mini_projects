from bs4 import BeautifulSoup

with open("index.htm") as fp:
    soup = BeautifulSoup(fp, 'html.parser')



#data_header = soup.table.tbody.tr

print(type(soup))
