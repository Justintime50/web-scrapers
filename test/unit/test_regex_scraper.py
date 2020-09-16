import mock
from web_scraper.regex_scraper import RegexScraper


def test_regex_scraper():
    phone = '(385) 203-7823'
    mock_open = mock.mock.mock_open(read_data=phone)
    with mock.mock.patch('builtins.open', mock_open):
        result = RegexScraper.run()
        assert phone in result
