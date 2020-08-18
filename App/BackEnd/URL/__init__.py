
from settings import URL
from App.BackEnd.Date import Date


class Url:

    __url = URL
    _date: Date
    _station_name: str

    def __init__(self, date: Date, station_name: str):
        self._station_name = station_name
        self.set_data(date)

    def get_date(self) -> Date:
        return self._date

    def set_data(self, date: Date):

        self._date = date
        day, month, year = date.get_date().day, date.get_date().month, date.get_date().year

        if day < 10:
            day = f"0{day}"

        if month < 10:
            month = f"0{month}"

        self.__url = self.__url.replace("$$$$$$$$", f"{year}{month}{day}")
        self.__url = self.__url.replace("#####", self._station_name)

    def get_url(self):
        return self.__url
