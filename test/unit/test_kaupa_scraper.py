import mock
from web_scrapers.kaupa_scraper import KaupaScraper


def test_kaupa_scraper():
    title = 'UNIVERSAL COOLING SYSTEM TESTER'
    mock_open = mock.mock.mock_open(read_data=title)
    with mock.mock.patch('builtins.open', mock_open):
        result = KaupaScraper.run()
        assert title in result[0]
