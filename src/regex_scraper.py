""" Scrape a webpage using Regex """
import re
import requests

# get the data
DATA = requests.get(
    'https://www.yellowpages.com/search?search_terms=plumber&geo_location_terms=Orem%2C+UT'
    )

# extract the phone numbers, emails, whatever
PHONES = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', DATA.text)
EMAILS = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', DATA.text)

print(PHONES, "\n", EMAILS, "\n\n", file=open("output.txt", "a"))
