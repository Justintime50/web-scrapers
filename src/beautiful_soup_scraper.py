""" Scrape a webpage using BeautifulSoup """
import requests
from bs4 import BeautifulSoup

# get the DATA
DATA = requests.get('https://umggaming.com/leaderboards')

# load DATA into bs4
SOUP = BeautifulSoup(DATA.text, 'html.parser')

LEADERBOARD = SOUP.find('table', {'id': 'leaderboard-table'})
TBODY = LEADERBOARD.find('tbody')

for tr in TBODY.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    username = tr.find_all('td')[1].find_all('a')[1].text.strip()
    xp = tr.find_all('td')[3].text.strip()
    print(place, username, xp)
