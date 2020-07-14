
from App.TxtConverter import TxtConverter
from App.ExtractData import ExtractData
from App.URL import Url


if __name__ == '__main__':

    date = input("Insira o ano, o mes e o dia - ex(20200703): ")
    u = Url(date)
    ext = ExtractData(u)
    ext.extract()
    txt = TxtConverter(ext.get_data())
    txt.write()
