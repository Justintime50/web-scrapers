"""Scrape a site using BeautifulSoup and iterate over ecommerce items"""
import requests
from bs4 import BeautifulSoup

X = 10

for i in range(X):
    try:

        # get the data
        # here we start at item 3974 and iterate for the variable X above
        data = requests.get(f'http://www.kaupa.com.tw/client/item_detail/autos/3/{3974+i}')

        # load data into bs4
        soup = BeautifulSoup(data.text, 'html.parser')

        title = soup.find('h2').text.strip()
        subtitle = soup.find('p', {'style': 'font-size:16px'}).text.strip()
        description = soup.find('div', {'class': 'product_detail_content'}).text.strip()

        print(title)
        print(subtitle)
        print(description)
        print("\n")
    except ValueError:
        print("Could not iterate the list provided.")
        break
