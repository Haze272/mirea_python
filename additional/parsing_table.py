import re
from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

url = 'https://www.mirea.ru/schedule/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

regex = '[И][И][Т][_][2]'
result_link = ''
for ana in soup.find_all('a', class_='uk-link-toggle'):
    res = re.findall(regex, ana.attrs["href"])
    for i in res:
        if i == 'ИИТ_2':
            result_link = ana.attrs["href"]

send = requests.get(result_link)
file = open('test.xlsx', 'wb')
file.write(send.content)
file.close()

schedule = pd.read_excel('test.xlsx')
schedule.head()

print(schedule["ИНБО-07-20"])