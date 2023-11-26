import requests
from bs4 import BeautifulSoup
import re


def parse_partners(partners_dict: dict[str, str], url: str) -> dict[str, str]:
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    partners = soup.find_all(
            'a',
            class_='partner-list-inner__name'
            )
    regex = re.compile(r'[\n\r\t ]')

    for partner in partners:
        name = regex.sub(' ', partner.text).strip()
        href = 'kstpro.ru' + partner.get('href')
        partners_dict[name] = href

    return partners_dict
# print(partners_dict)
