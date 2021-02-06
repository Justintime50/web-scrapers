import re

import requests


class RegexScraper():
    @classmethod
    def run(cls):
        """Scrape a webpage using Regex
        """
        data = requests.get(
            'https://www.yellowpages.com/search?search_terms=plumber&geo_location_terms=Orem%2C+UT'  # noqa
        )

        # Extract the phone numbers, emails, whatever
        phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)  # noqa
        # emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

        scraped_data = phones
        with open('output.txt', 'w') as output:
            output.write(str(scraped_data))

        print(scraped_data)
        return scraped_data


def main():
    RegexScraper.run()


if __name__ == '__main__':
    main()
