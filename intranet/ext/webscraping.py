from bs4 import BeautifulSoup
import requests


def bs(source):
    return BeautifulSoup(requests.get(source).content, "html.parser")
