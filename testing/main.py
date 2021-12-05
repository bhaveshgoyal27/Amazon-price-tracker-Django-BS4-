import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.in/Old-Spice-After-Shave-Lotion/dp/B00F2LF2GY/"

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    # print(soup.prettify())

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price

print(get_link_data(url))