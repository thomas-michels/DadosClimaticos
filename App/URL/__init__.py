
from settings import URL


class Url:

    __url = URL

    def __init__(self, data: str):
        self.set_data(data)

    def set_data(self, data: str):
        self.__url = self.__url.replace("$$$$$$$$", data)

    def get_url(self):
        return self.__url
