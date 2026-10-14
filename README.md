
# Project 5: Web Scraper

## Description
A Python web scraper that extracts headlines from a permitted
news webpage using Requests and BeautifulSoup and saves them
to a CSV file.

## Technologies Used
- Python
- Requests
- BeautifulSoup4
- CSV module

## Features
- Checks robots.txt before scraping
- Extracts webpage headings
- Removes duplicate headlines
- Saves headlines in CSV format
- Includes error handling and a request delay

## How to Run
1. Install Python.
2. Install dependencies:
   `python -m pip install requests beautifulsoup4`
3. Run:
   `python web_scraper.py`

## Output
The program creates `headlines.csv` when headlines are
successfully extracted.

## Author
Student Python Project
