import requests
import urllib.request
import time
from bs4 import BeautifulSoup

print('"State","County","City","Hospital","Url"')
for i in range(11, 19):
    url = 'https://oshpd.ca.gov/data-and-reports/cost-transparency/hospital-chargemasters/20' + str(i) + '-chargemasters'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select('table.tablepress > tbody tr')
    for row in rows:
        year = row.select('td.column-1')[0].text
        hospital = row.select('td.column-2')[0].text
        href = row.select('td.column-3 > a')[0].get('href')
        print('"California",,,"' + hospital + '","' + url + href + '"')
        
