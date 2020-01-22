<div align="center">

# Web Scraper

Scrape the contents of any site, customizable to your needs.

[![Build Status](https://travis-ci.org/Justintime50/web-scraper.svg?branch=master)](https://travis-ci.org/Justintime50/web-scraper)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.gif">

</div>

## Install

**NOTE:** Web Scraper requires Python3.

```bash
pip install -r requirements.txt
```

## Usage

Edit the scripts to suit your needs, then run them.

- `regex-scraper.py` - simple regex web scraper, quick and dirty approach.
- `beautiful-soup-scraper.py` - additional customization options available with Beautiful Soup.

**Example**
```bash
python beautiful-soup-scraper.py
```

The output of the scraped page will be saved to a `output.txt` file.

## Development & Testing

Install dependencies and run linting.

```bash
pylint src/*.py
```

## Attribution

Code based on the project from [Engineer Man](https://github.com/engineer-man/youtube/tree/master/042).
