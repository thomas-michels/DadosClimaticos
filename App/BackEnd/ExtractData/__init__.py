
from requests import get
from App.BackEnd.TxtConverter import TxtConverter
from settings import PATH


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
            data = []

            for url in self._urls:
                day_data = get(url.get_url()).json()
                data.append(day_data)

            txt = TxtConverter(data)
            file = txt.call_one_file(name)
            txt.write(file)

        else:

            for url in self._urls:
                data = get(url.get_url()).json()
                dat = data['observations']
                name = dat[0]['obsTimeUtc'][0:10]
                station = dat[0]['stationID']
                _path = PATH.replace(r'\dist\run', '')
                file = open(f"{_path}\Data\{station}_{name}.txt", 'a')
                txt = TxtConverter(dat[0])
                txt.header(file)
                file.close()

                for line in dat:
                    txt = TxtConverter(line)
                    file = txt.call_files(station, name)
                    txt.write(file, line)
