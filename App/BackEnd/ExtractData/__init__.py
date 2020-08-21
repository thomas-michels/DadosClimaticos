
from requests import get
from App.BackEnd.TxtConverter import TxtConverter


class ExtractData:

    def __init__(self, urls: list, is_one_file: bool):
        self._urls = urls
        self._is_one_file = is_one_file

    def extract_and_save(self):

        if self._is_one_file:

            init_date = self._urls[0].get_date().get_date()
            final_date = self._urls[-1].get_date().get_date()

            name = f'{init_date.year}-{init_date.month}-{init_date.day}' \
                   f'_{final_date.year}-{final_date.month}-{final_date.day}'

            for url in self._urls:
                data = get(url.get_url()).json()
                txt = TxtConverter(data)
                txt.write(txt.call_one_file(name))

        else:
            for url in self._urls:
                data = get(url.get_url()).json()
                txt = TxtConverter(data)
                txt.write(txt.call_files())
