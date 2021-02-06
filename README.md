<div align="center">

# Web Scrapers

A collection of web scrapers.

[![Build Status](https://github.com/Justintime50/web-scrapers/workflows/build/badge.svg)](https://github.com/Justintime50/web-scrapers/actions)
[![Licence](https://img.shields.io/github/license/justintime50/web-scrapers)](LICENSE)

<img src="assets/showcase.gif" alt="Showcase">

</div>

## Install

```bash
# Install locally
make install

# Get Makefile help
make help
```

## Usage

The scripts in this project are provided as a template or example - each webpage is different and would require tweaking these scripts to scrape the data you need.

* `beautiful-soup-scraper.py` - additional customization options available with Beautiful Soup.
* `kaupa_scraper.py` - an example of using BS4 on a website.
* `regex-scraper.py` - simple regex web scraper, quick and dirty approach.
* `scrape_ep_docs.py` - Scrapes the EasyPost documentation for 'predefined-packages' OR 'service-levels'.
* `scrape_iso_country_codes.py` - Scrapes the ISO country codes of countries around the world from Wikipedia.

```bash
venv/bin/python web_scrapers/beautiful_soup_scraper.py
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run the scripts locally
venv/bin/python web_scrapers/beautiful_soup_scraper.py
```

## Attribution

- Web scrapers initially based on the project from [Engineer Man](https://github.com/engineer-man/youtube/tree/master/042).
