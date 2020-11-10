
from settings import PATH


class TxtConverter:

    _path = PATH.replace(r'\dist\run', '')

    def __init__(self, data: list):
        self._data = data

    def header(self, file):
        file.write("stationID;tz;obsTimeUtc;obsTimeLocal;epoch;lat;lon;solarRadiationHigh;uvHigh;winddirAvg;")
        file.write("humidityHigh;humidityLow;humidityAvg;qcStatus;tempHigh;tempLow;windspeedHigh;windspeedLow;")
        file.write("windspeedAvg;windgustHigh;windgustLow;windgustAvg;dewptHigh;dewptLow;dewptAvg;")
        file.write("windchillHigh;windchillLow;windchillAvg;heatindexHigh;heatindexLow;heatindexAvg;")
        file.write("pressureMax;pressureMin;pressureTrend;precipRate;precipTotal\n")

    def call_one_file(self, name):
        file = open(f"{self._path}\Data\{self._data[0]['observations'][0]['stationID']}_{name}.txt", 'a')
        self.header(file)
        return file

    def call_files(self, station, name):
        return open(f"{self._path}\Data\{station}_{name}.txt", 'a')

    def write(self, file, dat=None):

        if dat is None:

            for data in self._data:
                data = data['observations']
                for line in data:
                    file.write(f"{line['stationID']};{line['tz']};{line['obsTimeUtc']};{line['obsTimeLocal']};{line['epoch']};"
                               f"{line['lat']};{line['lon']};{line['solarRadiationHigh']};{line['uvHigh']};"
                               f"{line['winddirAvg']};{line['humidityHigh']};{line['humidityLow']};{line['humidityAvg']};"
                               f"{line['qcStatus']};{line['metric']['tempHigh']};{line['metric']['tempLow']};"
                               f"{line['metric']['windspeedHigh']};{line['metric']['windspeedLow']};"
                               f"{line['metric']['windspeedAvg']};{line['metric']['windgustHigh']};"
                               f"{line['metric']['windgustLow']};{line['metric']['windgustAvg']};"
                               f"{line['metric']['dewptHigh']};{line['metric']['dewptLow']};{line['metric']['dewptAvg']};"
                               f"{line['metric']['windchillHigh']};{line['metric']['windchillLow']};"
                               f"{line['metric']['windchillAvg']};{line['metric']['heatindexHigh']};"
                               f"{line['metric']['heatindexLow']};{line['metric']['heatindexAvg']};"
                               f"{line['metric']['pressureMax']};{line['metric']['pressureMin']};"
                               f"{line['metric']['pressureTrend']};{line['metric']['precipRate']};"
                               f"{line['metric']['precipTotal']}\n")

        else:

            file.write(f"{dat['stationID']};{dat['tz']};{dat['obsTimeUtc']};{dat['obsTimeLocal']};{dat['epoch']};"
                       f"{dat['lat']};{dat['lon']};{dat['solarRadiationHigh']};{dat['uvHigh']};{dat['winddirAvg']};"
                       f"{dat['humidityHigh']};{dat['humidityLow']};{dat['humidityAvg']};{dat['qcStatus']};"
                       f"{dat['metric']['tempHigh']};{dat['metric']['tempLow']};{dat['metric']['windspeedHigh']};"
                       f"{dat['metric']['windspeedLow']};{dat['metric']['windspeedAvg']};"
                       f"{dat['metric']['windgustHigh']};{dat['metric']['windgustLow']};"
                       f"{dat['metric']['windgustAvg']};{dat['metric']['dewptHigh']};{dat['metric']['dewptLow']};"
                       f"{dat['metric']['dewptAvg']};{dat['metric']['windchillHigh']};"
                       f"{dat['metric']['windchillLow']};{dat['metric']['windchillAvg']};"
                       f"{dat['metric']['heatindexHigh']};{dat['metric']['heatindexLow']};"
                       f"{dat['metric']['heatindexAvg']};{dat['metric']['pressureMax']};"
                       f"{dat['metric']['pressureMin']};{dat['metric']['pressureTrend']};"
                       f"{dat['metric']['precipRate']};{dat['metric']['precipTotal']}\n")

        file.close()
