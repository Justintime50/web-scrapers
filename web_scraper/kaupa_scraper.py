import requests
from bs4 import BeautifulSoup


class KaupaScraper():
    @classmethod
    def run(cls):
        """Scrape a site using BeautifulSoup and iterate over ecommerce items
        """
        X = 10
        total_scraped_data = []

        for i in range(X):
            try:
                # Here we start at item 3974 and iterate for the variable X above  # noqa
                data = requests.get(
                    f'http://www.kaupa.com.tw/client/item_detail/autos/3/{3974+i}'  # noqa
                )

                # Load data into bs4
                soup = BeautifulSoup(data.text, 'html.parser')
                title = soup.find('h2').text.strip()
                subtitle = soup.find(
                    'p', {'style': 'font-size:16px'}).text.strip()
                description = soup.find(
                    'div', {'class': 'product_detail_content'}
                ).text.strip()

                scraped_data = title + '\n' + subtitle + '\n' + description + '\n\n'  # noqa
                total_scraped_data.append(scraped_data)
                with open('output.txt', 'a') as output:
                    output.write(scraped_data)

                print(scraped_data)
            except ValueError:
                message = 'Could not iterate the list provided.'
                print(message)
                return message
        return total_scraped_data


def main():
    KaupaScraper.run()


if __name__ == '__main__':
    main()
