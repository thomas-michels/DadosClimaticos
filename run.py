
from App.ExtractData import ExtractData
from App.Date import Date
from App.DateManager import DateManager


if __name__ == '__main__':

    dayID, mountID, yearID = input("Insira a data inicial (DD/MM/AAAA): ").split('/')
    dayFD, mountFD, yearFD = input("Insira a data final (DD/MM/AAAA): ").split('/')
    date = Date(dayID, mountID, yearID)
    date2 = Date(dayFD, mountFD, yearFD)
    dm = DateManager(date, date2)
    ext = ExtractData(dm.generate_url())
    ext.extract_and_save()

