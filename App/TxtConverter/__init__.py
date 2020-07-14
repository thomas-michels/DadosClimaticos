
from App.URL import Url
from App.ExtractData import ExtractData
from settings import PATH


class TxtConverter:

    _path = PATH.replace(r"\App", "")

    def __init__(self, data: dict):
        self._data = data

    def get_lines(self):

        return self._data['observations']

    def call_file(self, method: str):
        return open(f'{self._path}\App\Data\climate_data.txt', method)


if __name__ == '__main__':
    u = Url("20200703")
    ext = ExtractData(u)
    ext.extract()
    txt = TxtConverter(ext.get_data())
    txt.call_file('w').write("aaaa")
    print((txt._path))
