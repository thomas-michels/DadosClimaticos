
from App.Date import Date
from App.Exceptions import UnprocessableEntityException
import pendulum
from datetime import datetime


class DateManager:

    days_list = []

    def __init__(self, initial_date: Date, final_date: Date):
        self._initial_date = initial_date
        self._final_date = final_date
        self._check_dates()

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
