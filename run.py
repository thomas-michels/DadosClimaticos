
from App.TxtConverter import TxtConverter
from App.ExtractData import ExtractData
from App.URL import Url
from App.Date import Date


if __name__ == '__main__':

    day = input("Insert day: ")
    month = input("Insert month: ")
    year = input("Insert year: ")
    date = Date(day, month, year)
    url = Url(date)
    print(date.get_date())
    ext = ExtractData(url)
    ext.extract()
    txt = TxtConverter(ext.get_data())
    txt.write()
