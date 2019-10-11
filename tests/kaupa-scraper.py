import requests
from bs4 import BeautifulSoup

X = 10

for i in range(X):
    try:
        # get the data
        data = requests.get(f'http://www.kaupa.com.tw/client/item_detail/autos/3/{i}')

        # load data into bs4
        soup = BeautifulSoup(data.text, 'html.parser')

        title = soup.find('h2')
        subtitle = soup.find('p', { 'style': 'font-size:16px' })
        description = soup.find('div', { 'class': 'product_detail_content' })

        print(title).text.strip()
        print(subtitle).text.strip()
        print(description).text.strip()
    except:
        break
