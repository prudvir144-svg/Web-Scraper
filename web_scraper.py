
import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

URL = "https://www.bbc.com/news"
CSV_FILE = "headlines.csv"

HEADERS = {
    "User-Agent": "StudentHeadlineScraper/1.0 (educational project)"
}


def check_robots_permission(url):
    parsed_url = urlparse(url)
    robots_url = (
        f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    )

    parser = RobotFileParser()
    parser.set_url(robots_url)

    try:
        response = requests.get(
            robots_url, headers=HEADERS, timeout=15
        )
        response.raise_for_status()
        parser.parse(response.text.splitlines())

        return parser.can_fetch(HEADERS["User-Agent"], url)

    except requests.RequestException as error:
        print("Could not check robots.txt:", error)
        return False


def scrape_headlines():
    if not check_robots_permission(URL):
        print("Scraping is not confirmed as permitted. Stopping.")
        return

    time.sleep(2)

    try:
        response = requests.get(
            URL, headers=HEADERS, timeout=15
        )
        response.raise_for_status()

    except requests.RequestException as error:
        print("Error fetching webpage:", error)
        return

    soup = BeautifulSoup(response.text, "html.parser")
    headline_elements = soup.find_all("h2")

    headlines = []

    for element in headline_elements:
        headline = element.get_text(" ", strip=True)
        if headline:
            headlines.append(headline)

    headlines = list(dict.fromkeys(headlines))

    if not headlines:
        print("No headlines found. Check the webpage structure.")
        return

    with open(
        CSV_FILE, "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])

        for headline in headlines:
            writer.writerow([headline])

    print(f"Saved {len(headlines)} headlines to {CSV_FILE}")


if __name__ == "__main__":
    scrape_headlines()
