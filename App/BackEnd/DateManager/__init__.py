
from App.BackEnd.Date import Date
from App.BackEnd.Exceptions import UnprocessableEntityException
import pendulum
from datetime import datetime
from App.BackEnd.URL import Url


class DateManager:

    days_list = []
    _initial_date: Date
    _final_date: Date
    _station: str

    def __init__(self, initial_date: Date, final_date: Date, station: str):
        self._station = station
        self.set_initial_date(initial_date)
        self.set_final_date(final_date)
        self._check_dates()
        self.generate_period()

    def set_initial_date(self, initial_date: Date):
        self._initial_date = initial_date

    def set_final_date(self, final_date: Date):
        self._final_date = final_date

    def get_initial_date(self):
        return self._initial_date

    def get_final_date(self):
        return self._final_date

    def _check_dates(self):
        if self._initial_date.get_date() > self._final_date.get_date():
            raise UnprocessableEntityException()

    def generate_period(self):
        initial_date = datetime(self._initial_date.get_date().year,
                                self._initial_date.get_date().month,
                                self._initial_date.get_date().day)

        final_date = datetime(self._final_date.get_date().year,
                              self._final_date.get_date().month,
                              self._final_date.get_date().day)

        period = pendulum.period(initial_date, final_date)

        for days in period.range('days'):
            self.days_list.append(Date(days.day, days.month, days.year))

    def get_days_list(self):
        return self.days_list

    def generate_url(self):

        urls = []

        for date in self.days_list:
            urls.append(Url(date, self._station))

        return urls
