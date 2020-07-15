
from settings import URL
from App.Date import Date


class Url:

    __url = URL

    def __init__(self, date: Date):
        self.set_data(date)

    def set_data(self, date: Date):
        day, month, year = date.get_date().day, date.get_date().month, date.get_date().year

        if day < 10:
            day = f"0{day}"

        if month < 10:
            month = f"0{month}"

        self.__url = self.__url.replace("$$$$$$$$", f"{year}{month}{day}")
        print(self.__url)

    def get_url(self):
        return self.__url
