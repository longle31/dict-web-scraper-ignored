
# class _DictionaryWrappedData:
#     pass


class DictionaryWebScraperInterface:
    def __init__(self): pass

    def scrap(self, word: str):
        html_raw_data = self._get_html_raw_data(word)
        # meanings = self._extract_meanings(html_raw_data)
        # pronunciations = self._extract_pronunciations(html_raw_data)
        # examples = self._extract_examples(html_raw_data)
        # related_volcabularies = self._collect_related_vocabularies(html_raw_data)
        # return _DictionaryWrappedData(meanings, pronunciations, related_volcabularies, examples)
        return html_raw_data

    def _extract_pronunciations(self, html_raw_data: str):
        pass

    def _get_html_raw_data(self, word: str):
        pass

    def _extract_meanings(self, html_raw_data: str):
        pass

    def _collect_related_vocabularies(self, html_raw_data: str):
        pass
