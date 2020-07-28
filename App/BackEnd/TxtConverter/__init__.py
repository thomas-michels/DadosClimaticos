
from settings import PATH


class TxtConverter:

    _path = PATH

    def __init__(self, data: dict):
        self._data = data

    def _get_lines(self):

        return self._data['observations']

    def call_file(self, method: str):
        return open(
            f"{self._path}\App\BackEnd\Data\climate_data_{self._data['observations'][0]['obsTimeLocal'][0:10]}.txt", method)

    def write(self):
        data = self._get_lines()
        file = self.call_file('w')

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