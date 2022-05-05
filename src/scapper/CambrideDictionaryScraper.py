from DictionaryWebScraperInterface import DictionaryWebScraperInterface
import requests


class CambridgeDictionaryScraper(DictionaryWebScraperInterface):
    def __init__(self):
        super(CambridgeDictionaryScraper, self).__init__()
        
    def scrap(self, word: str):
        return super(CambridgeDictionaryScraper, self).scrap(word)

    def _extract_pronunciations(self, html_raw_data: str):
        pass

    def _get_html_raw_data(self, word: str) -> str:
        return requests.get('https://dictionary.cambridge.org/dictionary/english/' + word, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }).text

    def _extract_meanings(self, html_raw_data: str):
        pass

    def _collect_related_vocabularies(self, html_raw_data: str):
        pass
