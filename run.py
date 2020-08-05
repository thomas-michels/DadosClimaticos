
from App.BackEnd.ExtractData import ExtractData
from App.BackEnd.Date import Date
from App.BackEnd.DateManager import DateManager
from App.FrontEnd.main import Ui_main

if __name__ == '__main__':

    # dayID, mountID, yearID = input("Insira a data inicial (DD/MM/AAAA): ").split('/')
    # dayFD, mountFD, yearFD = input("Insira a data final (DD/MM/AAAA): ").split('/')
    # date = Date(dayID, mountID, yearID)
    # date2 = Date(dayFD, mountFD, yearFD)
    # dm = DateManager(date, date2)
    # ext = ExtractData(dm.generate_url(), False)
    # ext.extract_and_save()
    ui = Ui_main()
    ui.run()
