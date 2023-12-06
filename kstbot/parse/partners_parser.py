import requests as rq
from bs4 import BeautifulSoup


page = rq.get("https://kstpro.ru/company/partners/")
soup = BeautifulSoup(page.content, "lxml")


def parse_partners(partners_dict: dict[str, str]) -> dict[str, str]:
    block = soup.find("div", {"id": "bx_3218110189_240"})
    if block is None:
        return partners_dict
    for i in block.find_all("a"):
        partners_dict[i.text.strip()] = "kstpro.ru" + i.get("href")
    return partners_dict
