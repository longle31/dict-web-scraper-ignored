# from bs4 import BeautifulSoup
# import requests
#
# html_text = requests.get('https://dictionary.cambridge.org/dictionary/english/man',  headers={
# "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# }).text
# soup = BeautifulSoup(html_text, 'lxml')
# meanings = soup.find_all('div', class_='pr di superentry')
#
# def filter_meaning(meaning):
#     return  meaning.find('span', class_='hw dsense_hw')
#
# for meaning in meanings:
#     filtered_meaning = filter_meaning(meaning)
#     if(filtered_meaning):
#         print(filtered_meaning.text)
from DictionaryWebScraperInterface import DictionaryWebScraperInterface
from CambrideDictionaryScraper import CambridgeDictionaryScraper
scapper = CambridgeDictionaryScraper()

man = scapper.scrap('man')
print(man)
