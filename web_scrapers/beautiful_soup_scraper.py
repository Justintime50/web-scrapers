import requests
from bs4 import BeautifulSoup

# NOTE: This script is now broken (2020-09-15) due
# to the umggaming site putting up checks to stop scraping.
# However, this can still be used as a template


class BeautifulSoupScraper():
    @classmethod
    def run(cls):
        """Scrape a webpage using BeautifulSoup
        """
        data = requests.get('https://umggaming.com/leaderboards')

        # load DATA into bs4
        soup = BeautifulSoup(data.text, 'html.parser')

        leaderboard = soup.find('table', {'id': 'leaderboard-table'})
        tbody = leaderboard.find('tbody')
        total_scraped_data = []

        for tr in tbody.find_all('tr'):
            place = tr.find_all('td')[0].text.strip()
            username = tr.find_all('td')[1].find_all('a')[1].text.strip()
            xp = tr.find_all('td')[3].text.strip()
            scraped_data = place + username + xp
            total_scraped_data.append(scraped_data)

            with open("output.txt", "a") as output:
                output.write(scraped_data)
            print(scraped_data)
        return total_scraped_data


def main():
    BeautifulSoupScraper.run()


if __name__ == '__main__':
    main()
