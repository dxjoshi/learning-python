import requests
from bs4 import BeautifulSoup

url = 'http://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php'
indices_url = 'https://www.moneycontrol.com/stocksmarketsindia/'

data = requests.get(indices_url)
soup = BeautifulSoup(data.text, 'html.parser')

records = []
#   get data by looking at each tr
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    records.append(values)

# for entry in records:
#     print(entry)

records = []
#   get data by looking at each tr
table = soup.find_all('table')
# body = table.find('tbody')
# print(table)
for tr in table[1].find_all('tr'):
    row = [td.text for td in tr.find_all('td')]
    if row:
        index = row[0]
        closing_value = row[1]
        change = row[2]
        percent_change = row[3]
        print(index, closing_value, change, percent_change)
print('---')

print('-------')

# records = []
# for div in soup.find('div', {'class': 'tab-content'}):
#     print(div.text)
# for tr in soup.find('tr', {'class': 'rhsglTbl'}):
#    values = [td.text for td in tr.find_all('td')]
#    records.append(values)
