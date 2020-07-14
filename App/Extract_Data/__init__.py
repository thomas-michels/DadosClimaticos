
from App.URL import Url
from requests import get


class ExtractData:

    _data: dict

    def __init__(self, url: Url):
        self._url = url

    def extract(self):
        self._data = get(self._url.get_url()).json()

    def get_data(self):
        return self._data
