
from settings import PATH


class TxtConverter:

    _path = PATH.replace(r'\dist\run', '')

    def __init__(self, data: dict):
        self._data = data

    def _get_lines(self):

        return self._data['observations']

    def call_one_file(self, name):
        return open(
            f"{self._path}\Data\{self._data['observations'][0]['stationID']}_{name}.txt", 'a')

    def call_files(self):
        return open(
            f"{self._path}\Data\{self._data['observations'][0]['stationID']}_{self._data['observations'][0]['obsTimeLocal'][0:10]}.txt", 'w')

    def write(self, file):
        data = self._get_lines()

        file.write("stationID;tz;obsTimeUtc;obsTimeLocal;epoch;lat;lon;solarRadiationHigh;uvHigh;winddirAvg;")
        file.write("humidityHigh;humidityLow;humidityAvg;qcStatus;tempHigh;tempLow;windspeedHigh;windspeedLow;")
        file.write("windspeedAvg;windgustHigh;windgustLow;windgustAvg;dewptHigh;dewptLow;dewptAvg;")
        file.write("windchillHigh;windchillLow;windchillAvg;heatindexHigh;heatindexLow;heatindexAvg;")
        file.write("pressureMax;pressureMin;pressureTrend;precipRate;precipTotal\n")

        for line in data:
            file.write(f"{line['stationID']};{line['tz']};{line['obsTimeUtc']};{line['obsTimeLocal']};{line['epoch']};"
                       f"{line['lat']};{line['lon']};{line['solarRadiationHigh']};{line['uvHigh']};"
                       f"{line['winddirAvg']};{line['humidityHigh']};{line['humidityLow']};{line['humidityAvg']};"
                       f"{line['qcStatus']};{line['imperial']['tempHigh']};{line['imperial']['tempLow']};"
                       f"{line['imperial']['windspeedHigh']};{line['imperial']['windspeedLow']};"
                       f"{line['imperial']['windspeedAvg']};{line['imperial']['windgustHigh']};"
                       f"{line['imperial']['windgustLow']};{line['imperial']['windgustAvg']};"
                       f"{line['imperial']['dewptHigh']};{line['imperial']['dewptLow']};{line['imperial']['dewptAvg']};"
                       f"{line['imperial']['windchillHigh']};{line['imperial']['windchillLow']};"
                       f"{line['imperial']['windchillAvg']};{line['imperial']['heatindexHigh']};"
                       f"{line['imperial']['heatindexLow']};{line['imperial']['heatindexAvg']};"
                       f"{line['imperial']['pressureMax']};{line['imperial']['pressureMin']};"
                       f"{line['imperial']['pressureTrend']};{line['imperial']['precipRate']};"
                       f"{line['imperial']['precipTotal']}\n")

        file.close()
