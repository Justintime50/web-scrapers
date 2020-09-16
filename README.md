<div align="center">

# Web Scraper

Scrape the contents of a webpage, customizable to your needs.

[![Build Status](https://travis-ci.com/Justintime50/web-scraper.svg?branch=master)](https://travis-ci.com/Justintime50/web-scraper)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/web-scraper/badge.svg?branch=master)](https://coveralls.io/github/Justintime50/web-scraper?branch=master)
[![PyPi](https://img.shields.io/pypi/v/<PROJECT>)](https://pypi.org/project/<PROJECT>)
[![Licence](https://img.shields.io/github/license/justintime50/web-scraper)](LICENSE)

<img src="assets/showcase.gif" alt="Showcase">

</div>

## Install

```bash
# Install tool
# TODO: Not yet available on PyPi

# Install locally
make install

# Get Makefile help
make help
```

## Usage

The scripts in this project are provided as a template - each webpage is different and would require tweaking these scripts to scrape the data you need.

* `beautiful-soup-scraper.py` - additional customization options available with Beautiful Soup.
* `kaupa_scraper.py` - an example of using BS4 on a website.
* `regex-scraper.py` - simple regex web scraper, quick and dirty approach.

```bash
venv/bin/python web-scraper/beautiful_soup_scraper.py
```

The output of the scraped page will be saved to a `output.txt` file.

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run the scripts locally
venv/bin/python web-scraper/beautiful_soup_scraper.py
```

## Attribution

Code based on the project from [Engineer Man](https://github.com/engineer-man/youtube/tree/master/042).
