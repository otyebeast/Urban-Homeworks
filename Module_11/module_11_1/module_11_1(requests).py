from bs4 import BeautifulSoup
import requests

url = 'https://cbr.ru/currency_base/daily/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

valutes = soup.find('div', class_='table-wrapper')
curse= []
for valute in valutes:
    print(valute.text)

