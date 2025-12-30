import requests
import selectorlib



URL = "https://x.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape(url):
    """
    Scrape the web page
    :param url:
    :return:
    """
    r = requests.get(URL, headers=HEADERS)

    data = r.text

    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(data)


if __name__ == "__main__":
    scrape(URL)