
from requests import get
from App.BackEnd.TxtConverter import TxtConverter


class ExtractData:

    def __init__(self, urls: list):
        self._urls = urls

    def extract_and_save(self):
        for url in self._urls:
            data = get(url.get_url()).json()
            txt = TxtConverter(data)
            txt.write()
