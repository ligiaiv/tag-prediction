from bs4 import BeautifulSoup
import requests
import logging as log
import sys
from pprint import pprint
log.basicConfig(filename='example.log', filemode='w', level=log.DEBUG)


def parse_description(soup: BeautifulSoup):
    return soup.find_all("p", {"itemprop": "description"})[0].text


def parse_tags(soup: BeautifulSoup) -> [str]:
    elements = soup.find_all("span", {"itemprop": "genre"})
    return [el.text for el in elements]


def parse_title(soup: BeautifulSoup) -> [str]:
    return soup.find_all("h1")[0].text


def parse_html(soup: BeautifulSoup):
    return {"title": parse_title(soup),
            "description": parse_description(soup),
            "tags": parse_tags(soup)}


def download_page(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print(url, response.status_code)
        log.info("error {} in url {}".format(response.status_code, url))
        return
    soup = BeautifulSoup(response.content, "html.parser")
    info = parse_html(soup)
    log.info("{} info downloaded".format(info["title"]))
    return info

